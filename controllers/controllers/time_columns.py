#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Responsible module to create controllers.
"""


from ..base import BaseHandlerTimeColumns
from modules.common import auth_non_browser_based


# TIME COLUMNS

class APITimeColumns(BaseHandlerTimeColumns):

    # A list of URLs that can be use for the HTTP methods
    urls = [r"/api/time_columns/?(?P<param>[A-Za-z0-9-]+)?/",
            r"/api/time_columns/?(?P<param>[A-Za-z0-9-]+)?"]

    def get(self, param=None):
        self.get_method_api_resource()

    @auth_non_browser_based
    def post(self, param=None):
        self.post_method_api_resource(param)

    @auth_non_browser_based
    def put(self, param=None):
        self.put_method_api_resource(param)

    # @auth_non_browser_based
    # def delete(self, param=None):
    #     self.delete_method_api_resource(param)