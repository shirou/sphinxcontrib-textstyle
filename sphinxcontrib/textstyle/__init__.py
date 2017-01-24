# -*- coding: utf-8 -*-
"""
    sphinxcontrib.textstyle
    ~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2013 by WAKAYAMA Shirou
    :license: BSD, see LICENSE for details.
"""
from __future__ import absolute_import


def setup(app):
    from sphinxcontrib.textstyle import ruby, deleted, color, column

    # delegate to submodules
    ruby.setup(app)
    deleted.setup(app)
    color.setup(app)
    column.setup(app)
