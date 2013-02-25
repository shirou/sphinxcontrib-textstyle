# -*- coding: utf-8 -*-
"""
    sphinxcontrib.textstyle
    ~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2013 by WAKAYAMA Shirou
    :license: BSD, see LICENSE for details.
"""

import re

from docutils import nodes, utils

import rubytag
import deltag


def setup(app):
    # rubytag
    app.add_role('ruby', rubytag.rubytag_role)
    app.add_node(rubytag.RubyTag,
             html=(rubytag.visit_rubytag_node, rubytag.depart_rubytag_node),
             epub=(rubytag.visit_rubytag_node, rubytag.depart_rubytag_node))
    app.add_config_value('rubytag_rp_start', '(', 'env')
    app.add_config_value('rubytag_rp_end', ')', 'env')

    # deltag
    app.add_role('del', deltag.deltag_role)
    app.add_node(deltag.DelTag,
             html=(deltag.visit_deltag_node, deltag.depart_deltag_node),
             epub=(deltag.visit_deltag_node, deltag.depart_deltag_node))
