PLUGIN_PREFIX = '/video/plex-nose-example'

def Start():
    ''

def ValidatePrefs():
    pass

@handler(PLUGIN_PREFIX, PLUGIN_TITLE)
def GetEnv():
    import os

    env = str()
    for k, v in os.environ.iteritems():
        env += '%s="%s" ' % (k, v)

    return ObjectContainer(header = 'Plex ENV', message = env)
