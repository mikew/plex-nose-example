import plex_nose
from nose.tools import raises, with_setup
from plex_nose import sandbox as sandboxed

# Code/__init__.py is already imported, but Start() is not called.
class SimpleTests(plex_nose.TestCase):
    def test_can_translate():
        eq_('Plex/nose Example', str(title()))

    def test_can_json():
        eq_('Value', get_json()['key'])

class DictTests(plex_nose.TestCase):
    def test_dict_can_modify():
        Dict['some_data'] = True
        Dict.Save()
        ok_(method_using_dict())

    def test_dict_is_reset():
        eq_({}, Dict._dict)

# Code executed in the sandbox will not have access to file/open, to read a
# local file use plex_nose.publish_local_file and write the tests inside
# a function defined in the tests.
#
# Use plex_nose.publish_local_file(f, name = 'named') to avoid collisions.
class PublishLocalFileTests(plex_nose.TestCase):
    def setUp(self):
        plex_nose.publish_local_file('Contents/Tests/mocked_data')

    def test_mocked_file():
        nose.tools.eq_("heyo\n", mocked_data)

# The not-so-simple method of writing simple tests. At least you can use
# decorators from nose.tools here
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

@raises(AssertionError)
@sandboxed
def test_nose_decorators():
    eq_('expected', 'actual')
