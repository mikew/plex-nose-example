from plex_nose import sandbox as sandboxed

# Tests need to be wrapped so imported files get access to the classes and
# methods available to Plex channels.
# Code imported from Code/ should be imported inside the test.
@sandboxed
def test_can_translate():
    import some_code
    nose.tools.eq_('Plex/nose Example', str(some_code.title()))

@sandboxed
def test_can_json():
    import some_code
    nose.tools.eq_('Value', some_code.get_json()['key'])

@sandboxed
def test_does_fail():
    nose.tools.eq_('expected', 'actual')
