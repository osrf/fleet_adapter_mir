"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.prompt_api import PromptApi  # noqa: E501


class TestPromptApi(unittest.TestCase):
    """PromptApi unit test stubs"""

    def setUp(self):
        self.api = PromptApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_prompt_get(self):
        """Test case for prompt_get

        GET /prompt  # noqa: E501
        """
        pass

    def test_prompt_guid_get(self):
        """Test case for prompt_guid_get

        GET /prompt/{guid}  # noqa: E501
        """
        pass

    def test_prompt_guid_put(self):
        """Test case for prompt_guid_put

        PUT /prompt/{guid}  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
