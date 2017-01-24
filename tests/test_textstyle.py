# -*- coding: utf-8 -*-

from sphinx_testing import with_app


@with_app(srcdir='tests/templates/basic')
def test_build_html(app, status, warnings):
    app.build()
    print(status.getvalue(), warnings.getvalue())

    html = (app.outdir / 'index.html').read_text()
    print(html)

    # :ruby: role
    expected = ('A text having ruby: <ruby><rb>東京</rb>'
                '<rp>(</rp><rt>とうきょう</rt><rp>)</rp></ruby>')
    assert expected in html

    expected = 'A ruby not having ruby-text: 東京'
    assert expected in html

    # :del: role
    expected = 'A deleted text: <del>Delete</del>'
    assert expected in html

    # del directive
    expected = '<p><del>This is a deleted block.</del></p>'
    assert expected in html

    # :color: role
    expected = 'A colored text: <span style="color: red">Color changed</span>'
    assert expected in html

    # column directive
    expected = '<div class="column admonition">'
    assert expected in html
