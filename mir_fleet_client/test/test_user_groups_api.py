"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.user_groups_api import UserGroupsApi  # noqa: E501


class TestUserGroupsApi(unittest.TestCase):
    """UserGroupsApi unit test stubs"""

    def setUp(self):
        self.api = UserGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_groups_get(self):
        """Test case for user_groups_get

        GET /user_groups  # noqa: E501
        """
        pass

    def test_user_groups_guid_delete(self):
        """Test case for user_groups_guid_delete

        DELETE /user_groups/{guid}  # noqa: E501
        """
        pass

    def test_user_groups_guid_get(self):
        """Test case for user_groups_guid_get

        GET /user_groups/{guid}  # noqa: E501
        """
        pass

    def test_user_groups_guid_put(self):
        """Test case for user_groups_guid_put

        PUT /user_groups/{guid}  # noqa: E501
        """
        pass

    def test_user_groups_post(self):
        """Test case for user_groups_post

        POST /user_groups  # noqa: E501
        """
        pass

    def test_user_groups_user_group_guid_permissions_get(self):
        """Test case for user_groups_user_group_guid_permissions_get

        GET /user_groups/{user_group_guid}/permissions  # noqa: E501
        """
        pass

    def test_user_groups_user_group_guid_permissions_post(self):
        """Test case for user_groups_user_group_guid_permissions_post

        POST /user_groups/{user_group_guid}/permissions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()