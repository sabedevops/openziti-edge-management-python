"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.5
    Contact: help@openziti.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openziti_edge_management
from openziti_edge_management.model.authenticator_detail_all_of import AuthenticatorDetailAllOf
from openziti_edge_management.model.base_entity import BaseEntity
from openziti_edge_management.model.entity_ref import EntityRef
from openziti_edge_management.model.links import Links
from openziti_edge_management.model.tags import Tags
globals()['AuthenticatorDetailAllOf'] = AuthenticatorDetailAllOf
globals()['BaseEntity'] = BaseEntity
globals()['EntityRef'] = EntityRef
globals()['Links'] = Links
globals()['Tags'] = Tags
from openziti_edge_management.model.authenticator_detail import AuthenticatorDetail


class TestAuthenticatorDetail(unittest.TestCase):
    """AuthenticatorDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAuthenticatorDetail(self):
        """Test AuthenticatorDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AuthenticatorDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
