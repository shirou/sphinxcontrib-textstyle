#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title


class RubyTag(nodes.General, nodes.Element):
    pass


def visit_rubytag_node(self, node):
    if node.rt is None:  # if rt is not set, just write rb.
        self.body.append(node.rb)
        return

    try:
        self.body.append(self.starttag(node, 'ruby'))
        self.body.append(self.starttag(node, 'rb'))
        self.body.append(node.rb)
        self.body.append('</rb>')
        self.body.append(self.starttag(node, 'rp'))
        self.body.append(node.rp_start)
        self.body.append('</rp>')
        self.body.append(self.starttag(node, 'rt'))
        self.body.append(node.rt)
        self.body.append('</rt>')
        self.body.append(self.starttag(node, 'rp'))
        self.body.append(node.rp_end)
        self.body.append('</rp>')
        self.body.append('</ruby>')
    except:
        self.builder.warn('fail to load rubytag: %r' % node)
        raise nodes.SkipNode


def depart_rubytag_node(self, node):
    pass


def rubytag_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for rubytag."""
    text = utils.unescape(text)
    has_explicit, rb, rt = split_explicit_title(text)

    config = inliner.document.settings.env.config

    rubytag = RubyTag()
    rubytag.rb = rb
    rubytag.rt = rt
    rubytag.rp_start = config.rubytag_rp_start
    rubytag.rp_end = config.rubytag_rp_end

    if not has_explicit:
        rubytag.rt = None

    return [rubytag], []
