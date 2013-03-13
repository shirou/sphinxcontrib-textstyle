Text style extension README
=============================

This is a sphinx extension to use some text styles.

- Ruby Annotation
- del
- color

Ruby annotation is HTML 5 Ruby tag (http://www.w3.org/TR/ruby/), not ruby
computer language.


Setting
=======

Install
-------

::

   > pip install sphinxcontrib-textstyle


Configure Sphinx
----------------

To enable this extension, add ``sphinxcontrib.textstyle`` module to extensions
option at `conf.py`.

::

   # Enabled extensions
   extensions = ['sphinxcontrib.textstyle']


Roles
=====================

- ruby role makes ruby tag

  ::

     :ruby:`東京<とうきょう>`

  A first string becomes ruby base (<rb>) and a string which is inside
  <> becomes ruby text(<rt>).  For rubytag not supported browser such
  as Firefox, ( and ) are used to represent ruby text(<rp>). You can
  change this character in the conf.py. See below config section.

- rst:role: del

  Del role makes delete (<del>).

  ::

     :del:`Delete`

- rst:directive: del

  Del is also a directive.

  ::

     .. del::  delete note(not shown)

        This specification will be deleted


- rst:role: color

  Color role changes the text color by using <span style="color">.
  Please keep in mind about this may break the separation of content
  and presentation.

  ::

     :color:`Color changed<red>`



Config
=========================

- rubytag_rp_start
- rubytag_rp_end

These two variables specify chracters which present ruby text.

::

   rubytag_rp_start = '['
   rubytag_rp_end   = ']'


Repository
==========

https://bitbucket.org/r_rudi/sphinxcontrib-textstyle

License
========

The BSD 2-Clause License.

