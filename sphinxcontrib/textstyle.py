# -*- coding: utf-8 -*-
"""
    sphinxcontrib.textstyle
    ~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2013 by WAKAYAMA Shirou
    :license: BSD, see LICENSE for details.
"""
from __future__ import absolute_import


def setup(app):
    from sphinxcontrib import ruby, deltag, color

    # delegate to submodules
    ruby.setup(app)
    deltag.setup(app)
    color.setup(app)
