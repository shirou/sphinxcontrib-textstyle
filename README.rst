text style extension README
==========================

This is a sphinx extension to use some text styles.

- ruby-tag
- del


Setting
=======

Install
-------

.. code-block:: bash

   > easy_install sphinxcontrib-textstyle


Configure Sphinx
----------------

To enable this extension, add ``sphinxcontrib.textstyle`` module to extensions
option at :file:`conf.py`.

.. code-block:: python

   # Enabled extensions
   extensions = ['sphinxcontrib.textstyle']


Directives and Roles
=====================

.. rst:role: ruby

   ruby role makes ruby tag

      :ruby:`強敵<とも>`

.. rst:role: del

   del role makes delete.

      :del:`Delete`

Repository
==========



License
========

Apache

