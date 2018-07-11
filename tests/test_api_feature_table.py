#!/usr/bin/env python
# -*- coding: utf-8 -*-


from unittest import TestCase
from util.tester import UtilTester


# https://realpython.com/blog/python/testing-third-party-apis-with-mocks/

class TestAPIFeatureTable(TestCase):

    def setUp(self):
        # create a tester passing the unittest self
        self.tester = UtilTester(self)

    # feature_table - get

    def test_get_api_feature_table_return_all_feature_tables(self):
        expected = {
            'features': [
                {
                    'type': 'FeatureTable',
                    'f_table_name': 'layer_1001',
                    'properties': {'id': 'integer', 'end_date': 'timestamp without time zone', 'geom': 'geometry',
                                   'address': 'text', 'version': 'integer', 'changeset_id': 'integer',
                                   'start_date': 'timestamp without time zone'},
                    'geometry': {
                        'crs': {'type': 'name', 'properties': {'name': 'EPSG:4326'}},
                        'type': 'MULTIPOINT'
                    }
                },
                {
                    'type': 'FeatureTable',
                    'f_table_name': 'layer_1002',
                    'properties': {'id': 'integer', 'end_date': 'text', 'geom': 'geometry', 'address': 'text',
                                   'version': 'integer', 'changeset_id': 'integer',
                                   'start_date': 'timestamp without time zone'},
                    'geometry': {
                        'crs': {'type':'name', 'properties': {'name': 'EPSG:4326'}},
                        'type': 'MULTIPOINT'
                    }
                },
                {
                    'type': 'FeatureTable',
                    'f_table_name': 'layer_1003',
                    'properties': {'name': 'text', 'id': 'integer', 'end_date': 'timestamp without time zone',
                                   'geom': 'geometry', 'version': 'integer', 'changeset_id': 'integer',
                                   'start_date': 'timestamp without time zone'},
                    'geometry': {
                        'crs': {'type':'name', 'properties': {'name': 'EPSG:4326'}},
                        'type': 'MULTILINESTRING'
                    }
                },
                {
                    'type': 'FeatureTable',
                    'f_table_name': 'layer_1004',
                    'properties': {'name': 'text', 'id': 'integer', 'end_date': 'text', 'geom': 'geometry',
                                   'version': 'integer', 'changeset_id': 'integer', 'start_date': 'text'},
                    'geometry': {
                        'crs': {'type': 'name', 'properties': {'name': 'EPSG:4326'}},
                        'type': 'MULTILINESTRING'
                    }
                },
                {
                    'type': 'FeatureTable',
                    'f_table_name': 'layer_1005',
                    'properties': {'name': 'text', 'id': 'integer', 'end_date': 'text', 'geom': 'geometry',
                                   'version': 'integer', 'changeset_id': 'integer', 'start_date': 'text'},
                    'geometry': {
                        'crs': {'type': 'name', 'properties':{'name': 'EPSG:4326'}},
                        'type': 'MULTIPOLYGON'
                    }
                },
                {
                    'type': 'FeatureTable',
                    'f_table_name': 'layer_1006',
                    'properties': {'name': 'text', 'id': 'integer', 'end_date': 'integer', 'geom': 'geometry',
                                   'version': 'integer', 'changeset_id': 'integer', 'start_date': 'integer'},
                    'geometry': {
                        'crs': {'type': 'name', 'properties': {'name': 'EPSG:4326'}},
                        'type': 'MULTIPOLYGON'
                    }
                }
            ],
            'type': 'FeatureCollection'
        }

        self.tester.api_feature_table(expected)

    def test_get_api_feature_table_return_feature_table_by_f_table_name(self):
        expected = {
            'features': [
                {
                    'type': 'FeatureTable',
                    'f_table_name': 'layer_1003',
                    'properties': {'name': 'text', 'id': 'integer', 'end_date': 'timestamp without time zone',
                                   'geom': 'geometry', 'version': 'integer', 'changeset_id': 'integer',
                                   'start_date': 'timestamp without time zone'},
                    'geometry': {
                        'crs': {'type': 'name', 'properties': {'name': 'EPSG:4326'}},
                        'type': 'MULTILINESTRING'
                    }
                }
            ],
            'type': 'FeatureCollection'
        }

        self.tester.api_feature_table(expected, f_table_name="1003")

    # feature table - create and update

    def test_api_feature_table_create_and_update(self):
        # DO LOGIN
        self.tester.auth_login("miguel@admin.com", "miguel")

        f_table_name = 'addresses_1930'

        ##################################################
        # create a layer
        ##################################################
        layer = {
            'type': 'Layer',
            'properties': {'layer_id': -1, 'f_table_name': f_table_name, 'name': 'Addresses in 1930',
                           'description': '', 'source_description': '',
                           'reference': [1050, 1052], 'keyword': [1001, 1041]}
        }
        layer = self.tester.api_layer_create(layer)

        ####################################################################################################

        ##################################################
        # create the feature_table for the layer above
        ##################################################
        feature_table = {
            'type': 'FeatureTable',
            'f_table_name': f_table_name,
            'properties': {'id': 'integer', 'geom': 'geometry', 'version': 'integer', 'changeset_id': 'integer',
                           'start_date': 'timestamp without time zone', 'end_date': 'timestamp without time zone',
                           'address': 'text'},
            'geometry': {
                'crs': {'type': 'name', 'properties': {'name': 'EPSG:4326'}},
                'type': 'MULTIPOINT'
            }
        }

        self.tester.api_feature_table_create(feature_table)

        ##################################################
        # update the feature_table
        ##################################################

        ##################################################
        # the feature_table is automatically removed when delete its layer
        ##################################################

        ####################################################################################################

        ##################################################
        # delete the layer
        ##################################################
        # get the id of layer to SEARCH AND REMOVE it
        layer_id = layer["properties"]["layer_id"]

        # REMOVE THE layer AFTER THE TESTS
        self.tester.api_layer_delete(layer_id)

        # it is not possible to find the layer that just deleted
        self.tester.api_layer_error_404_not_found(layer_id=layer_id)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()


class TestAPIFeatureTableErrors(TestCase):

    def setUp(self):
        # create a tester passing the unittest self
        self.tester = UtilTester(self)

    # feature_table errors - get

    def test_get_api_feature_table_error_404_not_found(self):
        self.tester.api_feature_table_error_404_not_found(f_table_name="999")
        self.tester.api_feature_table_error_404_not_found(f_table_name="998")

    # feature_table errors - create
    """
    def test_post_api_temporal_columns_create_error_400_bad_request_attribute_already_exist(self):
        # DO LOGIN
        self.tester.auth_login("miguel@admin.com", "miguel")

        # try to insert a temporal_columns with a f_table_name that already exist
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_400_bad_request(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()
    
    def test_post_api_temporal_columns_create_error_400_bad_request_attribute_in_JSON_is_missing(self):
        # DO LOGIN
        self.tester.auth_login("miguel@admin.com", "miguel")

        # try to create a temporal_columns (without f_table_name)
        resource = {
            'properties': {'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_400_bad_request(resource)

        # try to create a temporal_columns (without start_date)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_400_bad_request(resource)

        # try to create a temporal_columns (without end_date)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'start_date': '1900-01-01',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_400_bad_request(resource)

        # try to create a temporal_columns (without end_date_column_name)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'start_date_column_name': 'start_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_400_bad_request(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()
        # try to do the test with a admin
        self.tester.auth_login("rodrigo@admin.com", "rodrigo")

        # try to create a temporal_columns (without start_date_column_name)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_400_bad_request(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()

    def test_post_api_temporal_columns_create_error_401_unauthorized_without_authorization_header(self):
        resource = {
            'properties': {'f_table_name': 'layer_1002', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_401_unauthorized(resource)
    
    def test_post_api_temporal_columns_create_error_403_forbidden_invalid_user_tries_to_create_a_temporal_columns(self):
        # DO LOGIN
        self.tester.auth_login("miguel@admin.com", "miguel")

        # try to insert a curator with user_id and keyword_id that already exist
        resource = {
            'properties': {'f_table_name': 'layer_1002', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_403_forbidden(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()

    # feature table errors - update
    
    def test_put_api_temporal_columns_error_400_bad_request_attribute_in_JSON_is_missing(self):
        # DO LOGIN
        self.tester.auth_login("miguel@admin.com", "miguel")

        # try to update a temporal_columns (without f_table_name)
        resource = {
            'properties': {'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_400_bad_request(resource)

        # try to update a temporal_columns (without start_date)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_400_bad_request(resource)

        # try to update a temporal_columns (without end_date)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'start_date': '1900-01-01',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_400_bad_request(resource)

        # try to update a temporal_columns (without end_date_column_name)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'start_date_column_name': 'start_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_400_bad_request(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()
        # try to do the test with an admin
        self.tester.auth_login("rodrigo@admin.com", "rodrigo")

        # try to update a temporal_columns (without start_date_column_name)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_400_bad_request(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()

    def test_put_api_temporal_columns_error_401_unauthorized_without_authorization_header(self):
        resource = {
            'properties': {'f_table_name': 'layer_1002', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_401_unauthorized(resource)

    def test_put_api_temporal_columns_error_403_forbidden_invalid_user_tries_to_create_a_temporal_columns(self):
        # DO LOGIN
        self.tester.auth_login("miguel@admin.com", "miguel")

        # try to update a temporal_columns with an invalid user
        resource = {
            'properties': {'f_table_name': 'layer_1002', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_type': 'timestamp', 'end_date_type': 'timestamp',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_403_forbidden(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()
    """


# It is not necessary to pyt the main() of unittest here,
# because this file will be call by run_tests.py