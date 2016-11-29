#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title, set_role_source_info


class ruby(nodes.General, nodes.Element, nodes.Inline):
    pass


def visit_ruby(self, node):
    paren_start = self.builder.config.rubytag_rp_start
    paren_end = self.builder.config.rubytag_rp_end

    self.body.append(self.starttag(node, 'ruby', suffix=''))
    self.body.append(self.starttag(node, 'rb', suffix=''))
    self.body.append(node['base'])
    self.body.append('</rb>')
    self.body.append(self.starttag(node, 'rp', suffix=''))
    self.body.append(paren_start)
    self.body.append('</rp>')
    self.body.append(self.starttag(node, 'rt', suffix=''))
    self.body.append(node['text'])
    self.body.append('</rt>')
    self.body.append(self.starttag(node, 'rp', suffix=''))
    self.body.append(paren_end)
    self.body.append('</rp>')
    self.body.append('</ruby>')
    raise nodes.SkipNode


def ruby_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for rubytag."""
    text = utils.unescape(text)
    has_explicit, base, text = split_explicit_title(text)

    if not has_explicit:
        # the role does not have ruby-text is converted to Text node
        node = nodes.Text(text)
    else:
        node = ruby(rawtext, base=base, text=text)

    set_role_source_info(inliner, lineno, node)
    return [node], []


def setup(app):
    app.add_role('ruby', ruby_role)
    app.add_node(ruby, html=(visit_ruby, None))
    app.add_config_value('rubytag_rp_start', '(', 'env')
    app.add_config_value('rubytag_rp_end', ')', 'env')
