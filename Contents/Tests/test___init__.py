import plex_nose
from nose.tools import raises, with_setup
from plex_nose import sandbox as sandboxed

# All tests need to be decorated
#
# Code/__init__.py is already imported, but Start() is not called.
@sandboxed
def test_can_translate():
    eq_('Plex/nose Example', str(title()))

# JSON, XML, HTTP, everything works.
@sandboxed
def test_can_json():
    eq_('Value', get_json()['key'])

# Standard nose decorators work.
@raises(AssertionError)
@sandboxed
def test_does_fail():
    eq_('expected', 'actual')

# Rest assured you're testing against a clean Dict.
@with_setup(plex_nose.stub_dict, plex_nose.reset_dict)
@sandboxed
def test_dict_is_clean():
    ok_('some_data' not in Dict)
    Dict['some_data'] = True
    Dict.Save()
    ok_('some_data' in Dict)

@with_setup(plex_nose.stub_dict, plex_nose.reset_dict)
@sandboxed
def test_dict_is_cleaned():
    ok_('some_data' not in Dict)

# Inherit from plex_nose.TestCase for simplicity.
class TestWithDict(plex_nose.TestCase):
    # TODO: can we remove these decorators?
    @sandboxed
    def test_dict_can_modify():
        Dict['some_data'] = True
        Dict.Save()
        ok_(method_using_dict())

    @sandboxed
    def test_dict_is_reset():
        eq_({}, Dict._dict)

# Code executed in the sandbox will not have access to file/open, to read a
# local file use plex_nose.publish_local_file and write the tests inside
# a function defined in the tests.
#
# Use plex_nose.publish_local_file(f, name = 'named') to avoid collisions.
def test_mocked_file():
    plex_nose.publish_local_file('Contents/Tests/mocked_data')

    @sandboxed
    def test():
        nose.tools.eq_("heyo\n", mocked_data)

    test()
