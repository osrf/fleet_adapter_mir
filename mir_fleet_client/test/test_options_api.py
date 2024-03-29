"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.options_api import OptionsApi  # noqa: E501


class TestOptionsApi(unittest.TestCase):
    """OptionsApi unit test stubs"""

    def setUp(self):
        self.api = OptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_path_guides_path_guide_guid_options_get(self):
        """Test case for path_guides_path_guide_guid_options_get

        GET /path_guides/{path_guide_guid}/options  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
