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
from openziti_edge_management.model.dial_bind import DialBind
from openziti_edge_management.model.roles import Roles
from openziti_edge_management.model.semantic import Semantic
from openziti_edge_management.model.tags import Tags
globals()['DialBind'] = DialBind
globals()['Roles'] = Roles
globals()['Semantic'] = Semantic
globals()['Tags'] = Tags
from openziti_edge_management.model.service_policy_create import ServicePolicyCreate


class TestServicePolicyCreate(unittest.TestCase):
    """ServicePolicyCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServicePolicyCreate(self):
        """Test ServicePolicyCreate"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServicePolicyCreate()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
