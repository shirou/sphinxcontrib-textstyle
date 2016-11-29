#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title, set_role_source_info


class color(nodes.General, nodes.TextElement, nodes.Inline):
    pass


def visit_color(self, node):
    style = "color: %s" % node['color']
    self.body.append(self.starttag(node, 'span', style=style, suffix=''))


def depart_color(self, node):
    self.body.append('</span>')


def color_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for color."""
    text = utils.unescape(text)
    has_explicit, text, colorspec = split_explicit_title(text)

    if not has_explicit:
        # the role does not have color-spec is converted to Text node
        node = nodes.Text(text)
    else:
        node = color(rawtext, text, color=colorspec)

    set_role_source_info(inliner, lineno, node)
    return [node], []


def setup(app):
    app.add_role('color', color_role)
    app.add_node(color, html=(visit_color, depart_color))
