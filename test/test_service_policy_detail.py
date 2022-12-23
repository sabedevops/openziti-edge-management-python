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
from openziti_edge_management.model.base_entity import BaseEntity
from openziti_edge_management.model.dial_bind import DialBind
from openziti_edge_management.model.links import Links
from openziti_edge_management.model.named_roles import NamedRoles
from openziti_edge_management.model.roles import Roles
from openziti_edge_management.model.semantic import Semantic
from openziti_edge_management.model.service_policy_detail_all_of import ServicePolicyDetailAllOf
from openziti_edge_management.model.tags import Tags
globals()['BaseEntity'] = BaseEntity
globals()['DialBind'] = DialBind
globals()['Links'] = Links
globals()['NamedRoles'] = NamedRoles
globals()['Roles'] = Roles
globals()['Semantic'] = Semantic
globals()['ServicePolicyDetailAllOf'] = ServicePolicyDetailAllOf
globals()['Tags'] = Tags
from openziti_edge_management.model.service_policy_detail import ServicePolicyDetail


class TestServicePolicyDetail(unittest.TestCase):
    """ServicePolicyDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServicePolicyDetail(self):
        """Test ServicePolicyDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServicePolicyDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
