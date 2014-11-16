#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title


class Color(nodes.General, nodes.Element):
    pass


def visit_color_node(self, node):
    if node.color is None:  # if not set, just write text.
        self.body.append(node.text)
        return

    try:
        self.body.append(self.starttag(node, 'span',
                                       node.text,
                                       style="color: " + node.color))
        self.body.append('</span>')
    except Exception as e:
        self.builder.warn('fail to load color: %r' % node)
        raise nodes.SkipNode


def depart_color_node(self, node):
    pass


def color_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for color."""
    text = utils.unescape(text)
    has_explicit, text, arg = split_explicit_title(text)

    color = Color()
    color.text = text
    color.color = arg

    if not has_explicit:
        color.color = None

    return [color], []
