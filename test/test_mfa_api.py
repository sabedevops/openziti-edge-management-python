"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.5
    Contact: help@openziti.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import openziti_edge_management
from openziti_edge_management.api.mfa_api import MFAApi  # noqa: E501


class TestMFAApi(unittest.TestCase):
    """MFAApi unit test stubs"""

    def setUp(self):
        self.api = MFAApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authenticate_mfa(self):
        """Test case for authenticate_mfa

        Complete MFA authentication  # noqa: E501
        """
        pass

    def test_create_mfa_recovery_codes(self):
        """Test case for create_mfa_recovery_codes

        For a completed MFA enrollment regenerate the recovery codes  # noqa: E501
        """
        pass

    def test_delete_mfa(self):
        """Test case for delete_mfa

        Disable MFA for the current identity  # noqa: E501
        """
        pass

    def test_detail_mfa(self):
        """Test case for detail_mfa

        Returns the current status of MFA enrollment  # noqa: E501
        """
        pass

    def test_detail_mfa_qr_code(self):
        """Test case for detail_mfa_qr_code

        Show a QR code for unverified MFA enrollments  # noqa: E501
        """
        pass

    def test_detail_mfa_recovery_codes(self):
        """Test case for detail_mfa_recovery_codes

        For a completed MFA enrollment view the current recovery codes  # noqa: E501
        """
        pass

    def test_enroll_mfa(self):
        """Test case for enroll_mfa

        Initiate MFA enrollment  # noqa: E501
        """
        pass

    def test_remove_identity_mfa(self):
        """Test case for remove_identity_mfa

        Remove MFA from an identitity  # noqa: E501
        """
        pass

    def test_verify_mfa(self):
        """Test case for verify_mfa

        Complete MFA enrollment by verifying a time based one time token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
