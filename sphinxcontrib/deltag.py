#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title


class DelTag(nodes.General, nodes.Element):
    pass


def visit_deltag_node(self, node):
    try:
        self.body.append(self.starttag(node, 'del'))
        self.body.append(node.text)
        self.body.append('</del>')
    except:
        self.builder.warn('fail to load deltag: %r' % node)
        raise nodes.SkipNode


def depart_deltag_node(self, node):
    pass


def deltag_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for deltag."""
    text = utils.unescape(text)

    deltag = DelTag()
    deltag.text = text

    return [deltag], []
