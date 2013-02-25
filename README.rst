Text style extension README
=============================

This is a sphinx extension to use some text styles.

- Ruby Annotation
- del

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

     :ruby:`強敵<とも>`

- rst:role: del

  del role makes delete.

  ::

     :del:`Delete`

Repository
==========

https://bitbucket.org/r_rudi/sphinxcontrib-textstyle

License
========

Apache

