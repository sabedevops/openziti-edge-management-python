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
from openziti_edge_management.model.tags import Tags
from openziti_edge_management.model.terminator_cost import TerminatorCost
from openziti_edge_management.model.terminator_precedence import TerminatorPrecedence
globals()['Tags'] = Tags
globals()['TerminatorCost'] = TerminatorCost
globals()['TerminatorPrecedence'] = TerminatorPrecedence
from openziti_edge_management.model.terminator_create import TerminatorCreate


class TestTerminatorCreate(unittest.TestCase):
    """TerminatorCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTerminatorCreate(self):
        """Test TerminatorCreate"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TerminatorCreate()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
