import some_code
from nose.tools import *

# This needs to be called on any module imported in Contents/Code
# in order for them to access JSON, HTTP, XML, et al.
import plex_nose
plex_nose.extend(some_code)

def test_can_translate():
    eq_('Plex/nose Example', str(some_code.title()))
