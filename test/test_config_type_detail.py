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
from openziti_edge_management.model.config_type_detail_all_of import ConfigTypeDetailAllOf
from openziti_edge_management.model.links import Links
from openziti_edge_management.model.tags import Tags
globals()['BaseEntity'] = BaseEntity
globals()['ConfigTypeDetailAllOf'] = ConfigTypeDetailAllOf
globals()['Links'] = Links
globals()['Tags'] = Tags
from openziti_edge_management.model.config_type_detail import ConfigTypeDetail


class TestConfigTypeDetail(unittest.TestCase):
    """ConfigTypeDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConfigTypeDetail(self):
        """Test ConfigTypeDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConfigTypeDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
