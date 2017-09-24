#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes, utils
from docutils.parsers.rst import Directive, directives
from sphinx.util.nodes import set_role_source_info
from sphinx.locale import _


class deleted(nodes.General, nodes.TextElement, nodes.Inline):
    pass


def visit_deleted(self, node):
    self.body.append(self.starttag(node, 'del', suffix=''))


def depart_deleted(self, node):
    self.body.append('</del>')


def deleted_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for del."""
    text = utils.unescape(text)
    node = deleted(rawtext, text)
    set_role_source_info(inliner, lineno, node)
    return [node], []


class DeletedDirective(Directive):
    has_content = True

    def run(self):
        text = '\n'.join(self.content[1:]).strip()

        para = nodes.paragraph()
        para += deleted(text, text)
        return [para]


def setup(app):
    app.add_role('del', deleted_role)
    app.add_node(deleted, html=(visit_deleted, depart_deleted))
    app.add_directive('del', DeletedDirective)
