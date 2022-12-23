"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.5
    Contact: help@openziti.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import openziti_edge_management
from openziti_edge_management.api.session_api import SessionApi  # noqa: E501


class TestSessionApi(unittest.TestCase):
    """SessionApi unit test stubs"""

    def setUp(self):
        self.api = SessionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_session(self):
        """Test case for delete_session

        Delete a session  # noqa: E501
        """
        pass

    def test_detail_session(self):
        """Test case for detail_session

        Retrieves a single session  # noqa: E501
        """
        pass

    def test_detail_session_route_path(self):
        """Test case for detail_session_route_path

        Retrieves a single session's router path  # noqa: E501
        """
        pass

    def test_list_sessions(self):
        """Test case for list_sessions

        List sessions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
