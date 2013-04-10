import plex_nose

class CommmonTests(plex_nose.TestCase):
    @classmethod
    def setUpClass(cls):
        plex_nose.publish_local_file('Contents/Tests/mosaic.html',
            name = 'mosaic')

    def test_url_for_section():
        common = SharedCodeService.common

        eq_(common.url_for_section('all'), 'http://www.gamespot.com/videos/')
        eq_(common.url_for_section('interviews'), 'http://www.gamespot.com/videos/interviews/')

    def test_final_video_url():
        common = SharedCodeService.common

        given_url = 'http://www.gamespot.com/dl_movie/file.mp4'

        # The 'Latest Video' at the top of each Mosaic page is a player,
        # so sometimes we already know the final url

        eq_(common.final_video_url(given_url), given_url)

    def test_final_video_url_extra():
        import mock
        common = SharedCodeService.common

        given_url = 'http://www.gamespot.com/some-media'
        expected  = 'http://www.gamespot.com/dl_movie/169_lost_between_levels_seattle.ipod.mp4?s=6406531&c=movie_ftp_&site=1&u=http%3A%2F%2Fdownload.gamespotcdn.com%2Fd8%2Fgsc%2F2013%2F04%2F169_lost_between_levels_seattle.ipod.mp4'

        @mock.patch.object(common.HTML, 'ElementFromURL', return_value = HTML.ElementFromString(mosaic))
        def test(mock_html):
            eq_(common.final_video_url(given_url), expected)
            mock_html.assert_called_once_with(given_url)

        test()
