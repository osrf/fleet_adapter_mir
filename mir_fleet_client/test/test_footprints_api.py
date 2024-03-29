"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.footprints_api import FootprintsApi  # noqa: E501


class TestFootprintsApi(unittest.TestCase):
    """FootprintsApi unit test stubs"""

    def setUp(self):
        self.api = FootprintsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_footprints_get(self):
        """Test case for footprints_get

        GET /footprints  # noqa: E501
        """
        pass

    def test_footprints_guid_delete(self):
        """Test case for footprints_guid_delete

        DELETE /footprints/{guid}  # noqa: E501
        """
        pass

    def test_footprints_guid_get(self):
        """Test case for footprints_guid_get

        GET /footprints/{guid}  # noqa: E501
        """
        pass

    def test_footprints_guid_put(self):
        """Test case for footprints_guid_put

        PUT /footprints/{guid}  # noqa: E501
        """
        pass

    def test_footprints_post(self):
        """Test case for footprints_post

        POST /footprints  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
