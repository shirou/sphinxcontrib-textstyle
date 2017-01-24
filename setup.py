# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains the text style Sphinx extension.

- ruby (ruby tag. not ruby-lang)
- del (role and directive)
- color
- column

'''

requires = ['Sphinx>=0.6', 'setuptools']

setup(
    name='sphinxcontrib-textstyle',
    version='0.2.2',
    url='http://bitbucket.org/r_rudi/sphinxcontrib-textstyle',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-textstyle',
    license='BSD',
    author='WAKAYAMA Shirou',
    author_email='shirou.faw@gmail.com',
    description='Sphinx "textstyle" extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
