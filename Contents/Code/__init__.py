PLUGIN_PREFIX = '/video/plex-nose-example'
import tutorial

def Start():
    pass

def ValidatePrefs():
    pass

@route('%s/env' % tutorial.consts.prefix)
def GetEnv():
    import os

    env = str()
    for k, v in os.environ.iteritems():
        env += '%s="%s" ' % (k, v)

    return ObjectContainer(header = 'Plex ENV', message = env)

def title():
    return L('title')

def get_json():
    obj = JSON.ObjectFromURL('https://raw.github.com/dominictarr/JSON.sh/master/test/valid/object.json')
    return obj

def method_using_dict():
    return 'some_data' in Dict
