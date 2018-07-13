#!/usr/bin/env python
# -*- coding: utf-8 -*-


from unittest import TestCase
from util.tester import UtilTester


# https://realpython.com/blog/python/testing-third-party-apis-with-mocks/

class TestAPITemporalColumns(TestCase):

    def setUp(self):
        # create a tester passing the unittest self
        self.tester = UtilTester(self)

    # temporal_columns - get
    
    def test_get_api_temporal_columns_return_all_temporal_columns(self):
        expected = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1001,
                        'start_date': '1869-01-01', 'end_date_mask_id': 1001, 'end_date': '1975-12-31',
                        'f_table_name': 'layer_1001', 'start_date_column_name': 'start_date'
                    }
                },
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1001,
                        'start_date': '1886-01-01', 'end_date_mask_id': 1001, 'f_table_name': 'layer_1002',
                        'start_date_column_name': 'start_date', 'end_date': '1890-12-31'
                    }
                },
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1001,
                        'start_date': '1920-01-01', 'end_date_mask_id': 1001, 'end_date': '1930-12-31',
                        'f_table_name': 'layer_1003', 'start_date_column_name': 'start_date',
                    }
                },
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1002,
                        'start_date': '1920-01-01', 'end_date_mask_id': 1002, 'f_table_name': 'layer_1004',
                        'start_date_column_name': 'start_date', 'end_date': '1920-12-31'
                    }
                },
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1002,
                        'start_date': '1920-01-01', 'end_date_mask_id': 1002, 'f_table_name': 'layer_1005',
                        'start_date_column_name': 'start_date', 'end_date': '1940-12-31'
                    }
                },
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1003,
                        'start_date': '1900-01-01', 'end_date_mask_id': 1003, 'f_table_name': 'layer_1006',
                        'start_date_column_name': 'start_date', 'end_date': '1930-12-31'
                    }
                }
            ]
        }

        self.tester.api_temporal_columns(expected)

    def test_get_api_temporal_columns_return_temporal_columns_by_f_table_name(self):
        expected = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1001,
                        'start_date': '1920-01-01', 'end_date_mask_id': 1001, 'end_date': '1930-12-31',
                        'f_table_name': 'layer_1003', 'start_date_column_name': 'start_date'
                    }
                }
            ]
        }

        self.tester.api_temporal_columns(expected, f_table_name="1003")

    def test_get_api_temporal_columns_return_temporal_columns_by_temporal_bounding_box(self):
        expected = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1002,
                        'start_date': '1920-01-01', 'end_date_mask_id': 1002, 'f_table_name': 'layer_1004',
                        'start_date_column_name': 'start_date', 'end_date': '1920-12-31'
                    }
                }
            ]
        }

        self.tester.api_temporal_columns(expected, start_date_gte='1890-01-01', end_date_lte='1920-12-31')

    def test_get_api_temporal_columns_return_temporal_columns_by_start_date_greater_than_or_equal(self):
        expected = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1001,
                        'start_date': '1920-01-01', 'end_date_mask_id': 1001, 'end_date': '1930-12-31',
                        'f_table_name': 'layer_1003', 'start_date_column_name': 'start_date',
                    }
                },
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1002,
                        'start_date': '1920-01-01', 'end_date_mask_id': 1002, 'f_table_name': 'layer_1004',
                        'start_date_column_name': 'start_date', 'end_date': '1920-12-31'
                    }
                },
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1002,
                        'start_date': '1920-01-01', 'end_date_mask_id': 1002, 'f_table_name': 'layer_1005',
                        'start_date_column_name': 'start_date', 'end_date': '1940-12-31'
                    }
                }
            ]
        }

        self.tester.api_temporal_columns(expected, start_date_gte="1910-01-01")

    def test_get_api_temporal_columns_return_temporal_columns_by_end_date_less_than_or_equal(self):
        expected = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1001,
                        'start_date': '1886-01-01', 'end_date_mask_id': 1001, 'f_table_name': 'layer_1002',
                        'start_date_column_name': 'start_date', 'end_date': '1890-12-31'
                    }
                },
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1002,
                        'start_date': '1920-01-01', 'end_date_mask_id': 1002, 'f_table_name': 'layer_1004',
                        'start_date_column_name': 'start_date', 'end_date': '1920-12-31'
                    }
                }
            ]
        }

        self.tester.api_temporal_columns(expected, end_date_lte="1920-12-31")

    def test_get_api_temporal_columns_return_temporal_columns_by_start_date(self):
        expected = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1003,
                        'start_date': '1900-01-01', 'end_date_mask_id': 1003, 'f_table_name': 'layer_1006',
                        'start_date_column_name': 'start_date', 'end_date': '1930-12-31'
                    }
                }
            ]
        }

        self.tester.api_temporal_columns(expected, start_date="1900-01-01")

    def test_get_api_temporal_columns_return_temporal_columns_by_end_date(self):
        expected = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'TemporalColumns',
                    'properties': {
                        'end_date_column_name': 'end_date', 'start_date_mask_id': 1002,
                        'start_date': '1920-01-01', 'end_date_mask_id': 1002, 'f_table_name': 'layer_1004',
                        'start_date_column_name': 'start_date', 'end_date': '1920-12-31'
                    }
                }
            ]
        }

        self.tester.api_temporal_columns(expected, end_date="1920-12-31")
    
    # temporal_columns - create and update

    def test_api_temporal_columns_create_and_update(self):
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
        # create the time columns for the layer above
        ##################################################
        temporal_columns = {
            'properties': {'f_table_name': f_table_name, 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }

        self.tester.api_temporal_columns_create(temporal_columns)

        ##################################################
        # update the time columns
        ##################################################
        temporal_columns["properties"]["start_date"] = '1920-01-01'
        self.tester.api_temporal_columns_update(temporal_columns)

        ##################################################
        # the time columns is automatically removed when delete its layer
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

    def test_api_temporal_columns_create_and_update_with_admin(self):
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
                           'reference': [1050, 1052], 'keyword': [1001, 1041]},
        }
        layer = self.tester.api_layer_create(layer)

        ####################################################################################################

        # create the time columns with an admin user
        self.tester.auth_logout()
        self.tester.auth_login("rodrigo@admin.com", "rodrigo")

        ##################################################
        # create the time columns for the layer above
        ##################################################
        temporal_columns = {
            'properties': {'f_table_name': f_table_name, 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create(temporal_columns)

        ##################################################
        # update the time columns
        ##################################################
        temporal_columns["properties"]["start_date"] = '1920-01-01'
        self.tester.api_temporal_columns_update(temporal_columns)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()
        # DO LOGIN
        self.tester.auth_login("miguel@admin.com", "miguel")

        ##################################################
        # the time columns is automatically removed when delete its layer
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


class TestAPITemporalColumnsErrors(TestCase):

    def setUp(self):
        # create a tester passing the unittest self
        self.tester = UtilTester(self)

    # temporal_columns errors - get

    def test_get_api_temporal_columns_error_400_bad_request_invalid_date_format(self):
        self.tester.api_temporal_columns_error_400_bad_request(start_date="1910/01-01")
        self.tester.api_temporal_columns_error_400_bad_request(end_date="1910-01/01")
        self.tester.api_temporal_columns_error_400_bad_request(start_date_gte="1910/01=01")
        self.tester.api_temporal_columns_error_400_bad_request(end_date_lte="1910-01)01")

    def test_get_api_temporal_columns_error_404_not_found(self):
        self.tester.api_temporal_columns_error_404_not_found(f_table_name="layer_x")
        self.tester.api_temporal_columns_error_404_not_found(start_date="1800-01-01")
        self.tester.api_temporal_columns_error_404_not_found(end_date="2000-01-01")
        self.tester.api_temporal_columns_error_404_not_found(start_date_gte="2000-01-01")
        self.tester.api_temporal_columns_error_404_not_found(end_date_lte="1800-01-01")
    
    # temporal_columns errors - create

    def test_post_api_temporal_columns_create_error_400_bad_request_attribute_already_exist(self):
        # DO LOGIN
        self.tester.auth_login("miguel@admin.com", "miguel")

        # try to insert a temporal_columns with a f_table_name that already exist
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
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
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_400_bad_request(resource)

        # try to create a temporal_columns (without start_date)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_400_bad_request(resource)

        # try to create a temporal_columns (without end_date)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'start_date': '1900-01-01',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_400_bad_request(resource)

        # try to create a temporal_columns (without end_date_column_name)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'start_date_column_name': 'start_date',
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
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_400_bad_request(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()

    def test_post_api_temporal_columns_create_error_401_unauthorized_user_is_not_logged(self):
        resource = {
            'properties': {'f_table_name': 'layer_1002', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_401_unauthorized(resource)
    
    def test_post_api_temporal_columns_create_error_403_forbidden_invalid_user_tries_to_manage(self):
        # DO LOGIN
        self.tester.auth_login("miguel@admin.com", "miguel")

        # try to insert a curator with user_id and keyword_id that already exist
        resource = {
            'properties': {'f_table_name': 'layer_1002', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_403_forbidden(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()

    def test_post_api_temporal_columns_create_error_404_not_found_f_table_name_doesnt_exist(self):
        # DO LOGIN
        self.tester.auth_login("miguel@admin.com", "miguel")

        # try to insert a curator with user_id and keyword_id that already exist
        resource = {
            'properties': {'f_table_name': 'address', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_create_error_404_not_found(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()

    # temporal_columns errors - update
    
    def test_put_api_temporal_columns_error_400_bad_request_attribute_in_JSON_is_missing(self):
        # DO LOGIN
        self.tester.auth_login("miguel@admin.com", "miguel")

        # try to update a temporal_columns (without f_table_name)
        resource = {
            'properties': {'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_400_bad_request(resource)

        # try to update a temporal_columns (without start_date)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_400_bad_request(resource)

        # try to update a temporal_columns (without end_date)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'start_date': '1900-01-01',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_400_bad_request(resource)

        # try to update a temporal_columns (without end_date_column_name)
        resource = {
            'properties': {'f_table_name': 'layer_1003', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'start_date_column_name': 'start_date',
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
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_400_bad_request(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()

    def test_put_api_temporal_columns_error_401_unauthorized_user_is_not_logged(self):
        resource = {
            'properties': {'f_table_name': 'layer_1002', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_401_unauthorized(resource)

    def test_put_api_temporal_columns_error_403_forbidden_invalid_user_tries_to_manage(self):
        # DO LOGIN
        self.tester.auth_login("miguel@admin.com", "miguel")

        # try to update a temporal_columns with an invalid user
        resource = {
            'properties': {'f_table_name': 'layer_1002', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_403_forbidden(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()

    def test_put_api_temporal_columns_error_404_not_found_f_table_name_doesnt_exist(self):
        # DO LOGIN
        self.tester.auth_login("miguel@admin.com", "miguel")

        # try to update a temporal_columns with an invalid user
        resource = {
            'properties': {'f_table_name': 'address', 'start_date': '1900-01-01', 'end_date': '1920-12-31',
                           'end_date_column_name': 'end_date', 'start_date_column_name': 'start_date',
                           'start_date_mask_id': 1001, 'end_date_mask_id': 1001},
            'type': 'TemporalColumns'
        }
        self.tester.api_temporal_columns_update_error_404_not_found(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()


# It is not necessary to pyt the main() of unittest here,
# because this file will be call by run_tests.py
