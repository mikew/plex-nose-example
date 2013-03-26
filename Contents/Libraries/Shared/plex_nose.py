config = dict()

def bridge(**kwargs):
    global config

    for key, val in kwargs.iteritems():
        if not key in config: config[key] = val

def extend(base):
    for key, val in config.iteritems():
        setattr(base, key, val)
