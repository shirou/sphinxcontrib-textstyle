#!/usr/bin/env python
# -*- coding: utf-8 -*-


from docutils.parsers.rst.directives.admonitions import Admonition
from docutils import nodes
from sphinx.locale import _


class ColumnDirective(Admonition):
    node_class = nodes.admonition
    required_arguments = 1

    def run(self):
        self.arguments[0] = self.arguments[0]
        self.options.setdefault('class', []).append(self.name)
        r = Admonition.run(self)
        r[0]['name'] = self.name
        return r


def setup(app):
    app.add_directive('column', ColumnDirective)
