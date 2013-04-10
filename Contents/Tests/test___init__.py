import plex_nose

# Code/__init__.py is already imported, but Start() is not called.
class SimpleTests(plex_nose.TestCase):
    def test_can_translate():
        eq_(str(title()), 'Plex/nose Example')

    def test_can_json():
        eq_(get_json()['key'], 'Value')

class DictTests(plex_nose.TestCase):
    def test_dict_can_modify():
        Dict['some_data'] = True
        Dict.Save()
        ok_(method_using_dict())

    def test_dict_is_reset():
        ok_('some_data' not in Dict)

# Code executed in the sandbox will not have access to file/open, to read a
# local file use plex_nose.publish_local_file and write the tests inside
# a function defined in the tests.
#
# Use plex_nose.publish_local_file(f, name = 'named') to avoid collisions.
class PublishLocalFileTests(plex_nose.TestCase):
    @classmethod
    def setUpClass(cls):
        plex_nose.publish_local_file('Contents/Tests/mocked_data')

    def test_mocked_file():
        eq_(mocked_data, "heyo\n")

# The not-so-simple method of writing simple tests. At least you can use
# decorators from nose.tools here
from nose.tools import raises
from plex_nose import sandbox as sandboxed

@sandboxed
def test_dict_is_clean():
    Dict['some_data'] = True
    Dict.Save()
    ok_('some_data' in Dict)
    ok_('some_other_data' not in Dict)

@sandboxed
def test_dict_is_cleaned():
    ok_('some_data' not in Dict)

@raises(AssertionError)
@sandboxed
def test_nose_decorators():
    eq_('given', 'expected')
