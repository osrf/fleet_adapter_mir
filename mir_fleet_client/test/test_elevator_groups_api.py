"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.elevator_groups_api import ElevatorGroupsApi  # noqa: E501


class TestElevatorGroupsApi(unittest.TestCase):
    """ElevatorGroupsApi unit test stubs"""

    def setUp(self):
        self.api = ElevatorGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_elevator_groups_get(self):
        """Test case for elevator_groups_get

        GET /elevator_groups  # noqa: E501
        """
        pass

    def test_elevator_groups_group_id_elevators_elevator_guid_delete(self):
        """Test case for elevator_groups_group_id_elevators_elevator_guid_delete

        DELETE /elevator_groups/{group_id}/elevators/{elevator_guid}  # noqa: E501
        """
        pass

    def test_elevator_groups_group_id_elevators_get(self):
        """Test case for elevator_groups_group_id_elevators_get

        GET /elevator_groups/{group_id}/elevators  # noqa: E501
        """
        pass

    def test_elevator_groups_group_id_elevators_post(self):
        """Test case for elevator_groups_group_id_elevators_post

        POST /elevator_groups/{group_id}/elevators  # noqa: E501
        """
        pass

    def test_elevator_groups_group_id_robots_get(self):
        """Test case for elevator_groups_group_id_robots_get

        GET /elevator_groups/{group_id}/robots  # noqa: E501
        """
        pass

    def test_elevator_groups_group_id_robots_post(self):
        """Test case for elevator_groups_group_id_robots_post

        POST /elevator_groups/{group_id}/robots  # noqa: E501
        """
        pass

    def test_elevator_groups_group_id_robots_robot_id_delete(self):
        """Test case for elevator_groups_group_id_robots_robot_id_delete

        DELETE /elevator_groups/{group_id}/robots/{robot_id}  # noqa: E501
        """
        pass

    def test_elevator_groups_id_delete(self):
        """Test case for elevator_groups_id_delete

        DELETE /elevator_groups/{id}  # noqa: E501
        """
        pass

    def test_elevator_groups_id_get(self):
        """Test case for elevator_groups_id_get

        GET /elevator_groups/{id}  # noqa: E501
        """
        pass

    def test_elevator_groups_id_put(self):
        """Test case for elevator_groups_id_put

        PUT /elevator_groups/{id}  # noqa: E501
        """
        pass

    def test_elevator_groups_post(self):
        """Test case for elevator_groups_post

        POST /elevator_groups  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
