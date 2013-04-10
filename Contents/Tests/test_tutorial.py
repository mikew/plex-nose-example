import plex_nose

class TutorialTest(plex_nose.TestCase):
    @classmethod
    def setUpClass(cls):
        # Used in test_mosaic_menu
        plex_nose.publish_local_file('Contents/Tests/mosaic.html',
            name = 'mosaic')

    def test_main_menu():
        container = tutorial.MainMenu()

        eq_('title', container.title1._key)
        eq_(7, len(container.objects))

        i = 0
        for section in tutorial.main_sections:
            subject = container.objects[i]
            callback = Callback(tutorial.MosaicMenu, section = section)

            eq_('title.%s' % section, subject.title._key)
            eq_(callback, subject.key)

            i += 1

    def test_mosaic_menu():
        # This may look wild, but it means our test won't actually hit
        # the network, so we get (a) faster tests and (b) consistent
        # data to test against
        import mock
        @mock.patch.object(HTML, 'ElementFromURL', return_value = HTML.ElementFromString(mosaic))
        def test(mock_html):
            container = tutorial.MosaicMenu('all')

            eq_('title.all', container.title1._key)
            eq_(24, len(container.objects))

            # Ensure MosaicMenu calls HTML.ElementFromURL
            mock_html.assert_called_once_with('http://www.gamespot.com/videos/?page=1')
