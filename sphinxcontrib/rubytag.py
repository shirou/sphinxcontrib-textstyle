#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title


class RubyTag(nodes.General, nodes.Element):
    pass


def visit_rubytag_node(self, node):
    paren_start = self.builder.config.rubytag_rp_start
    paren_end = self.builder.config.rubytag_rp_end

    self.body.append(self.starttag(node, 'ruby', suffix=''))
    self.body.append(self.starttag(node, 'rb', suffix=''))
    self.body.append(node.rb)
    self.body.append('</rb>')
    self.body.append(self.starttag(node, 'rp', suffix=''))
    self.body.append(paren_start)
    self.body.append('</rp>')
    self.body.append(self.starttag(node, 'rt', suffix=''))
    self.body.append(node.rt)
    self.body.append('</rt>')
    self.body.append(self.starttag(node, 'rp', suffix=''))
    self.body.append(paren_end)
    self.body.append('</rp>')
    self.body.append('</ruby>')
    raise nodes.SkipNode


def rubytag_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for rubytag."""
    text = utils.unescape(text)
    has_explicit, rb, rt = split_explicit_title(text)

    if not has_explicit:
        # the role does not have ruby-text is converted to Text node
        text = nodes.Text(text)
        return [text], []
    else:
        rubytag = RubyTag()
        rubytag.rb = rb
        rubytag.rt = rt
        return [rubytag], []


def setup(app):
    app.add_role('ruby', rubytag_role)
    app.add_node(RubyTag,
                 html=(visit_rubytag_node, None),
                 epub=(visit_rubytag_node, None))
    app.add_config_value('rubytag_rp_start', '(', 'env')
    app.add_config_value('rubytag_rp_end', ')', 'env')
