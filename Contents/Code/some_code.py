@route('/asdfasdf/helo')
def title(): return L('title')

def get_json():
    obj = JSON.ObjectFromURL('https://raw.github.com/dominictarr/JSON.sh/master/test/valid/object.json')
    return obj
