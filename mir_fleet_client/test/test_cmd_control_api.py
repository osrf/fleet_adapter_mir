"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.cmd_control_api import CmdControlApi  # noqa: E501


class TestCmdControlApi(unittest.TestCase):
    """CmdControlApi unit test stubs"""

    def setUp(self):
        self.api = CmdControlApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_elevators_guid_cmd_control_post(self):
        """Test case for elevators_guid_cmd_control_post

        POST /elevators/{guid}/cmd_control  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
