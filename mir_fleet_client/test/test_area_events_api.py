"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.area_events_api import AreaEventsApi  # noqa: E501


class TestAreaEventsApi(unittest.TestCase):
    """AreaEventsApi unit test stubs"""

    def setUp(self):
        self.api = AreaEventsApi()  # noqa: E501

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

    def test_area_events_definitions_get(self):
        """Test case for area_events_definitions_get

        GET /area_events/definitions  # noqa: E501
        """
        pass

    def test_area_events_get(self):
        """Test case for area_events_get

        GET /area_events  # noqa: E501
        """
        pass

    def test_area_events_guid_blocked_put(self):
        """Test case for area_events_guid_blocked_put

        PUT /area_events/{guid}/blocked  # noqa: E501
        """
        pass

    def test_area_events_guid_delete(self):
        """Test case for area_events_guid_delete

        DELETE /area_events/{guid}  # noqa: E501
        """
        pass

    def test_area_events_guid_get(self):
        """Test case for area_events_guid_get

        GET /area_events/{guid}  # noqa: E501
        """
        pass

    def test_area_events_guid_put(self):
        """Test case for area_events_guid_put

        PUT /area_events/{guid}  # noqa: E501
        """
        pass

    def test_area_events_post(self):
        """Test case for area_events_post

        POST /area_events  # noqa: E501
        """
        pass

    def test_maps_map_id_area_events_get(self):
        """Test case for maps_map_id_area_events_get

        GET /maps/{map_id}/area_events  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
