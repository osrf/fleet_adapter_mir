"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.definitions_api import DefinitionsApi  # noqa: E501


class TestDefinitionsApi(unittest.TestCase):
    """DefinitionsApi unit test stubs"""

    def setUp(self):
        self.api = DefinitionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_area_events_definitions_get(self):
        """Test case for area_events_definitions_get

        GET /area_events/definitions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()