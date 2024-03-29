"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.qualified_robots_api import QualifiedRobotsApi  # noqa: E501


class TestQualifiedRobotsApi(unittest.TestCase):
    """QualifiedRobotsApi unit test stubs"""

    def setUp(self):
        self.api = QualifiedRobotsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_missions_guid_qualified_robots_get(self):
        """Test case for missions_guid_qualified_robots_get

        GET /missions/{guid}/qualified_robots  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
