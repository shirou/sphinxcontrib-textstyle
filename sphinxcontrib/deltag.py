#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title
from sphinx.util.compat import Directive


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


class DelDirective(Directive):
    has_content = True

    def run(self):
        deltag = DelTag()
        # delete first line which is option
        deltag.text = '\n'.join(self.content[1:])
        return [deltag]
