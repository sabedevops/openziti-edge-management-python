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
from openziti_edge_management.model.attributes import Attributes
from openziti_edge_management.model.entity_ref import EntityRef
from openziti_edge_management.model.env_info import EnvInfo
from openziti_edge_management.model.identity_authenticators import IdentityAuthenticators
from openziti_edge_management.model.identity_enrollments import IdentityEnrollments
from openziti_edge_management.model.sdk_info import SdkInfo
from openziti_edge_management.model.tags import Tags
from openziti_edge_management.model.terminator_cost import TerminatorCost
from openziti_edge_management.model.terminator_cost_map import TerminatorCostMap
from openziti_edge_management.model.terminator_precedence import TerminatorPrecedence
from openziti_edge_management.model.terminator_precedence_map import TerminatorPrecedenceMap
globals()['Attributes'] = Attributes
globals()['EntityRef'] = EntityRef
globals()['EnvInfo'] = EnvInfo
globals()['IdentityAuthenticators'] = IdentityAuthenticators
globals()['IdentityEnrollments'] = IdentityEnrollments
globals()['SdkInfo'] = SdkInfo
globals()['Tags'] = Tags
globals()['TerminatorCost'] = TerminatorCost
globals()['TerminatorCostMap'] = TerminatorCostMap
globals()['TerminatorPrecedence'] = TerminatorPrecedence
globals()['TerminatorPrecedenceMap'] = TerminatorPrecedenceMap
from openziti_edge_management.model.identity_detail_all_of import IdentityDetailAllOf


class TestIdentityDetailAllOf(unittest.TestCase):
    """IdentityDetailAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIdentityDetailAllOf(self):
        """Test IdentityDetailAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IdentityDetailAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
