import some_code

PLUGIN_PREFIX = '/video/plex-nose-example'

def Start():
    pass

def ValidatePrefs():
    pass

@handler(PLUGIN_PREFIX, some_code.title())
def GetEnv():
    import os

    env = str()
    for k, v in os.environ.iteritems():
        env += '%s="%s" ' % (k, v)

    return ObjectContainer(header = 'Plex ENV', message = env)
