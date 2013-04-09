import plex_nose

@plex_nose.sandbox
def test_url_for_section():
    consts = SharedCodeService.consts

    eq_('http://www.gamespot.com/videos/',
            consts.url_for_section('all'))
    eq_('http://www.gamespot.com/videos/interviews/',
            consts.url_for_section('interviews'))
