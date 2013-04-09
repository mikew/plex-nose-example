common = SharedCodeService.common
consts = SharedCodeService.consts
main_sections = [ 'all', 'interviews', 'reviews', 'gameplay', 'shows',
'trailers', 'previews' ]

@handler(consts.prefix, consts.title)
def MainMenu():
    container = ObjectContainer(title1 = L('title'))

    for section in main_sections:
        title  = L('title.%s' % section)
        cb     = Callback(MosaicMenu, section = section)
        button = DirectoryObject(title = title, key = cb)

        container.add(button)

    return container

@route('%s/{section}' % consts.prefix)
def MosaicMenu(section, page = 1):
    container = ObjectContainer(title1 = L('title.%s' % section))
    url       = common.url_for_section(section) + '?page=%s' % page
    root      = HTML.ElementFromURL(url)
    videos    = root.cssselect(consts.mosaic_selector)
    latest    = common.video_from_player(root)

    if latest:
        video = VideoClipObject(title = latest['title'], url = latest['url'])

        container.add(video)

    for video in videos:
        url   = common.permalink_for(video.get('href'))
        title = video.text_content().strip()
        video = VideoClipObject(title = title, url = url)

        container.add(video)

    return container
