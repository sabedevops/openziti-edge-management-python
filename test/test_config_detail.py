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
from openziti_edge_management.model.config_detail_all_of import ConfigDetailAllOf
from openziti_edge_management.model.entity_ref import EntityRef
from openziti_edge_management.model.links import Links
from openziti_edge_management.model.tags import Tags
globals()['BaseEntity'] = BaseEntity
globals()['ConfigDetailAllOf'] = ConfigDetailAllOf
globals()['EntityRef'] = EntityRef
globals()['Links'] = Links
globals()['Tags'] = Tags
from openziti_edge_management.model.config_detail import ConfigDetail


class TestConfigDetail(unittest.TestCase):
    """ConfigDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConfigDetail(self):
        """Test ConfigDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConfigDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
