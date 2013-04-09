import consts

main_sections = [ 'all', 'interviews', 'reviews', 'gameplay', 'shows',
'trailers', 'previews' ]
print SharedCodeService.test

def MainMenu():
    container = ObjectContainer(title1 = L('title'))

    for section in main_sections:
        title  = L('title.%s' % section)
        cb     = Callback(MosiacMenu, section = section)
        button = DirectoryObject(title = title, key = cb)

        container.add(button)

    return container

@route('%s/{section}' % consts.prefix)
def MosiacMenu(section, page = 1):
    container = ObjectContainer(title1 = L('title.%s' % section))
    url       = url_for_section(section) + '?page=%s' % page
    root      = HTML.ElementFromURL(url)
    videos    = root.cssselect('#video_stream a')
    latest    = root.cssselect('h1.video_title')

    if latest:
        url   = root.cssselect('#flash_req_msg video')[0].get('src')
        title = latest[0].text_content().strip()
        video = VideoClipObject(title = title, url = url)

        container.add(video)

    for video in videos:
        url   = 'http://www.gamespot.com' + video.get('href')
        title = video.text_content().strip()
        video = VideoClipObject(title = title, url = url)

        container.add(video)

    return container

def url_for_section(section):
    base_url = 'http://www.gamespot.com/videos/'

    if 'all' == section:
        return base_url
    else:
        return base_url + section + '/'
