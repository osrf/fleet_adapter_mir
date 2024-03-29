"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.docking_offsets_api import DockingOffsetsApi  # noqa: E501


class TestDockingOffsetsApi(unittest.TestCase):
    """DockingOffsetsApi unit test stubs"""

    def setUp(self):
        self.api = DockingOffsetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_docking_offsets_get(self):
        """Test case for docking_offsets_get

        GET /docking_offsets  # noqa: E501
        """
        pass

    def test_docking_offsets_guid_delete(self):
        """Test case for docking_offsets_guid_delete

        DELETE /docking_offsets/{guid}  # noqa: E501
        """
        pass

    def test_docking_offsets_guid_get(self):
        """Test case for docking_offsets_guid_get

        GET /docking_offsets/{guid}  # noqa: E501
        """
        pass

    def test_docking_offsets_guid_put(self):
        """Test case for docking_offsets_guid_put

        PUT /docking_offsets/{guid}  # noqa: E501
        """
        pass

    def test_docking_offsets_post(self):
        """Test case for docking_offsets_post

        POST /docking_offsets  # noqa: E501
        """
        pass

    def test_docking_offsets_shelfs_get(self):
        """Test case for docking_offsets_shelfs_get

        GET /docking_offsets/shelfs  # noqa: E501
        """
        pass

    def test_docking_offsets_types_get(self):
        """Test case for docking_offsets_types_get

        GET /docking_offsets/types  # noqa: E501
        """
        pass

    def test_docking_offsets_types_id_get(self):
        """Test case for docking_offsets_types_id_get

        GET /docking_offsets/types/{id}  # noqa: E501
        """
        pass

    def test_positions_pos_id_docking_offsets_get(self):
        """Test case for positions_pos_id_docking_offsets_get

        GET /positions/{pos_id}/docking_offsets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
