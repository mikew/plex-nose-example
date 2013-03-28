import plex_nose
from nose.tools import raises
from plex_nose  import sandbox as sandboxed

# Tests need to be wrapped so imported files get access to the classes and
# methods available to Plex channels.
# Code imported from Code/ should be imported inside the test.
@sandboxed
def test_can_translate():
    import __init__ as channel_code
    eq_('Plex/nose Example', str(channel_code.title()))

@sandboxed
def test_can_json():
    import __init__ as channel_code
    eq_('Value', channel_code.get_json()['key'])

@raises(AssertionError)
@sandboxed
def test_does_fail():
    eq_('expected', 'actual')

# Code executed in the sandbox will not have access to file/open, to read a
# local file use plex_nose.publish_local_file and write the tests inside
# a function defined in the tests.
def test_mocked_file():
    plex_nose.publish_local_file('Contents/Tests/mocked_data')

    @sandboxed
    def test():
        nose.tools.eq_("heyo\n", mocked_data)

    test()
