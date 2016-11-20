# -*- coding: utf-8 -*-
"""
    sphinxcontrib.textstyle
    ~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2013 by WAKAYAMA Shirou
    :license: BSD, see LICENSE for details.
"""
from __future__ import absolute_import

import re
from docutils import nodes, utils

from sphinxcontrib import rubytag, deltag, color


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
    app.add_directive('del', deltag.DelDirective)

    # style="color"
    app.add_role('color', color.color_role)
    app.add_node(color.Color,
             html=(color.visit_color_node, color.depart_color_node),
             epub=(color.visit_color_node, color.depart_color_node))
