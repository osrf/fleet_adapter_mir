"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.action_definitions_api import ActionDefinitionsApi  # noqa: E501


class TestActionDefinitionsApi(unittest.TestCase):
    """ActionDefinitionsApi unit test stubs"""

    def setUp(self):
        self.api = ActionDefinitionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_area_events_action_definitions_action_type_get(self):
        """Test case for area_events_action_definitions_action_type_get

        GET /area_events/action_definitions/{action_type}  # noqa: E501
        """
        pass

    def test_area_events_action_definitions_get(self):
        """Test case for area_events_action_definitions_get

        GET /area_events/action_definitions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
