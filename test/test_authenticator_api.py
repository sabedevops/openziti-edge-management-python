"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.5
    Contact: help@openziti.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import openziti_edge_management
from openziti_edge_management.api.authenticator_api import AuthenticatorApi  # noqa: E501


class TestAuthenticatorApi(unittest.TestCase):
    """AuthenticatorApi unit test stubs"""

    def setUp(self):
        self.api = AuthenticatorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_authenticator(self):
        """Test case for create_authenticator

        Creates an authenticator  # noqa: E501
        """
        pass

    def test_delete_authenticator(self):
        """Test case for delete_authenticator

        Delete an Authenticator  # noqa: E501
        """
        pass

    def test_detail_authenticator(self):
        """Test case for detail_authenticator

        Retrieves a single authenticator  # noqa: E501
        """
        pass

    def test_list_authenticators(self):
        """Test case for list_authenticators

        List authenticators  # noqa: E501
        """
        pass

    def test_patch_authenticator(self):
        """Test case for patch_authenticator

        Update the supplied fields on an authenticator  # noqa: E501
        """
        pass

    def test_re_enroll_authenticator(self):
        """Test case for re_enroll_authenticator

        Reverts an authenticator to an enrollment  # noqa: E501
        """
        pass

    def test_update_authenticator(self):
        """Test case for update_authenticator

        Update all fields on an authenticator  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
