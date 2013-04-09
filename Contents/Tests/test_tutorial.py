import plex_nose

class TutorialTest(plex_nose.TestCase):
    @classmethod
    def setUpClass(cls):
        # This saves us from writing `import tutorial` at the start of
        # each test
        plex_nose.core.sandbox.execute('import tutorial')

        # Used in test_mosiac_menu
        plex_nose.publish_local_file('Contents/Tests/mosiac.html', 
                name = 'mosiac')

    def test_main_menu():
        container = tutorial.MainMenu()

        eq_('title', container.title1._key)
        eq_(7, len(container.objects))

        i = 0
        for section in tutorial.main_sections:
            subject = container.objects[i]
            eq_('title.%s' % section, subject.title._key)
            ok_('/%s' % section in subject.key)
            i += 1

    def test_url_for_section():
        eq_('http://www.gamespot.com/videos/',
                tutorial.url_for_section('all'))
        eq_('http://www.gamespot.com/videos/interviews/',
                tutorial.url_for_section('interviews'))

    def test_mosiac_menu():
        # This may look wild, but it means our test won't actually hit
        # the network, so we get (a) faster tests and (b) consistent
        # data to test against
        import mock
        m = mock.MagicMock(return_value = HTML.ElementFromString(mosiac))
        om_ = HTML.ElementFromURL
        HTML.ElementFromURL = m

        container = tutorial.MosiacMenu('all')

        # Ensure MosiacMenu calls HTML.ElementFromURL
        m.assert_called_once_with('http://www.gamespot.com/videos/?page=1')

        eq_('title.all', container.title1._key)
        eq_(24, len(container.objects))

        # Restore our mocks
        HTML.ElementFromURL = om_
