"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.import_api import ImportApi  # noqa: E501


class TestImportApi(unittest.TestCase):
    """ImportApi unit test stubs"""

    def setUp(self):
        self.api = ImportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sessions_import_delete(self):
        """Test case for sessions_import_delete

        DELETE /sessions/import  # noqa: E501
        """
        pass

    def test_sessions_import_get(self):
        """Test case for sessions_import_get

        GET /sessions/import  # noqa: E501
        """
        pass

    def test_sessions_import_post(self):
        """Test case for sessions_import_post

        POST /sessions/import  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
