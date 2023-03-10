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
from openziti_edge_management.model.ca_detail_all_of import CaDetailAllOf
from openziti_edge_management.model.external_id_claim import ExternalIdClaim
from openziti_edge_management.model.links import Links
from openziti_edge_management.model.roles import Roles
from openziti_edge_management.model.tags import Tags
globals()['BaseEntity'] = BaseEntity
globals()['CaDetailAllOf'] = CaDetailAllOf
globals()['ExternalIdClaim'] = ExternalIdClaim
globals()['Links'] = Links
globals()['Roles'] = Roles
globals()['Tags'] = Tags
from openziti_edge_management.model.ca_detail import CaDetail


class TestCaDetail(unittest.TestCase):
    """CaDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCaDetail(self):
        """Test CaDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CaDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
