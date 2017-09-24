import os

import pytest
from sphinx.testing.path import path


import os
import sys
testroot = os.path.dirname(__file__) or '.'
sys.path.insert(0, os.path.abspath(os.path.join(testroot, os.path.pardir)))
print(sys.path)

pytest_plugins = 'sphinx.testing.fixtures'


@pytest.fixture(scope='session')
def rootdir():
    return path(os.path.dirname(__file__) or '.').abspath() / 'roots'
