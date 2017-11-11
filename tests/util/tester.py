#!/usr/bin/env python
# -*- coding: utf-8 -*-


from json import loads, dumps
from requests import Session


def by_multi_element_get_url_name(multi_element):
    if multi_element == "MultiPoint":
        return "node"
    if multi_element == "MultiLineString":
        return "way"
    if multi_element == "MultiPolygon":
        return "area"

    raise Exception("Invalid multi element: {0}".format(multi_element))


class UtilTester:

    def __init__(self, ut_self):
        # create a session, simulating a browser. It is necessary to create cookies on server
        self.session = Session()
        # headers
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        # unittest self
        self.ut_self = ut_self

    def do_login(self):
        response = self.session.get('http://localhost:8888/auth/login/fake/')

        self.ut_self.assertEqual(response.status_code, 200)

    def do_logout(self):
        response = self.session.get('http://localhost:8888/auth/logout')

        self.ut_self.assertEqual(response.status_code, 200)

    # project

    def create_project(self, project_json):
        # do a GET call, sending a changeset to add in DB
        response = self.session.put('http://localhost:8888/api/project/create/',
                                    data=dumps(project_json), headers=self.headers)

        resulted = loads(response.text)  # convert string to dict/JSON

        self.ut_self.assertIn("id", resulted)
        self.ut_self.assertNotEqual(resulted["id"], -1)

        # put the id received in the original JSON of changeset
        project_json["project"]["properties"]["id"] = resulted["id"]

        return project_json

    def delete_project(self, project):
        # get the id of project to REMOVE it
        fk_id_project = project["project"]["properties"]["id"]

        response = self.session.delete('http://localhost:8888/api/project/delete/{0}'.format(fk_id_project))

        self.ut_self.assertEqual(response.status_code, 200)

    # changeset

    def create_changeset(self, changeset_json):
        # do a GET call, sending a changeset to add in DB
        response = self.session.put('http://localhost:8888/api/changeset/create/',
                                    data=dumps(changeset_json), headers=self.headers)

        resulted = loads(response.text)  # convert string to dict/JSON

        self.ut_self.assertIn("id", resulted)
        self.ut_self.assertNotEqual(resulted["id"], -1)

        # put the id received in the original JSON of changeset
        changeset_json["changeset"]["properties"]["id"] = resulted["id"]

        return changeset_json

    def close_changeset(self, changeset):
        # get the id of changeset to CLOSE the changeset
        fk_id_changeset = changeset["changeset"]["properties"]["id"]

        response = self.session.put('http://localhost:8888/api/changeset/close/{0}'.format(fk_id_changeset))

        self.ut_self.assertEqual(response.status_code, 200)

    # element

    def add_element(self, element_json):
        multi_element = element_json["features"][0]["geometry"]["type"]
        element = by_multi_element_get_url_name(multi_element)

        # do a PUT call, sending a node to add in DB
        response = self.session.put('http://localhost:8888/api/{0}/create/'.format(element),
                                    data=dumps(element_json), headers=self.headers)

        resulted = loads(response.text)  # convert string to dict/JSON

        self.ut_self.assertIn("id", resulted)
        self.ut_self.assertNotEqual(resulted["id"], -1)

        # put the id received in the original JSON of node
        element_json["features"][0]["properties"]["id"] = resulted["id"]

        return element_json

    def delete_element(self, element_json):
        id_element = element_json["features"][0]["properties"]["id"]  # get the id of element

        multi_element = element_json["features"][0]["geometry"]["type"]
        element = by_multi_element_get_url_name(multi_element)

        response = self.session.delete('http://localhost:8888/api/{0}/?q=[id={1}]'.format(element, id_element))

        self.ut_self.assertEqual(response.status_code, 200)

    def verify_if_element_was_add_in_db(self, element_json_expected):
        id_element = element_json_expected["features"][0]["properties"]["id"]  # get the id of element

        multi_element = element_json_expected["features"][0]["geometry"]["type"]

        element = by_multi_element_get_url_name(multi_element)

        # do a GET call with default format (GeoJSON)
        response = self.session.get('http://localhost:8888/api/{0}/?q=[id={1}]'.format(element, id_element))

        self.ut_self.assertTrue(response.ok)
        self.ut_self.assertEqual(response.status_code, 200)

        resulted = loads(response.text)  # convert string to dict/JSON

        self.ut_self.assertEqual(element_json_expected, resulted)

    def verify_if_element_was_not_add_in_db(self, element_json_expected):
        id_element = element_json_expected["features"][0]["properties"]["id"]  # get the id of element

        multi_element = element_json_expected["features"][0]["geometry"]["type"]
        element = by_multi_element_get_url_name(multi_element)

        # do a GET call with default format (GeoJSON)
        response = self.session.get('http://localhost:8888/api/{0}/?q=[id={1}]'.format(element, id_element))

        self.ut_self.assertEqual(response.status_code, 404)