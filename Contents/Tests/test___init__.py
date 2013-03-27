import plex_nose
from nose.tools import raises
from plex_nose  import sandbox as sandboxed

# Tests need to be wrapped so imported files get access to the classes and
# methods available to Plex channels.
# Code imported from Code/ should be imported inside the test.
def test_can_translate():
    @sandboxed
    def test():
        import __init__ as channel_code
        nose.tools.eq_('Plex/nose Example', str(channel_code.title()))

    test()

def test_can_json():
    @sandboxed
    def test():
        import __init__ as channel_code
        nose.tools.eq_('Value', channel_code.get_json()['key'])

    test()

@raises(AssertionError)
def test_does_fail():
    @sandboxed
    def test():
        nose.tools.eq_('expected', 'actual')

    test()

# Code executed in the sandbox will not have access to file/open, to read a
# local file use plex_nose.publish_local_file and write the tests inside
# a function defined in the tests.
def test_mocked_file():
    plex_nose.publish_local_file('Contents/Tests/mocked_data')

    @sandboxed
    def test():
        nose.tools.eq_("heyo\n", mocked_data)

    test()
