"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.download_api import DownloadApi  # noqa: E501


class TestDownloadApi(unittest.TestCase):
    """DownloadApi unit test stubs"""

    def setUp(self):
        self.api = DownloadApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_log_error_reports_id_download_get(self):
        """Test case for log_error_reports_id_download_get

        GET /log/error_reports/{id}/download  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
