from functools import wraps

import os
import nose
import unittest

import Framework

run_once_ = False
def run_once():
    global run_once_
    if run_once_ is False:
        core.sandbox.publish_api(nose)
        core.sandbox.publish_api(nose.tools.eq_)
        core.sandbox.publish_api(nose.tools.ok_)
        run_once_ = True

def stub_dict():
    _dict = Framework.api.datakit.DictKit(core.sandbox)
    _dict._dict_path = core.bundle_path + '/Contents/Tests/Dict'
    _dict.Save = lambda : True

    core.sandbox.publish_api(_dict, name = 'Dict')

def reset_dict():
    core.sandbox.call_named_function('Reset', mod_name = 'Dict', raise_exceptions = True)

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls): run_once()
    def setUp(self):     stub_dict()
    def tearDown(self):  reset_dict()

def publish_local_file(local_path, name = None):
    local_path = os.path.abspath(core.bundle_path + '/' + local_path)
    local_file = open(local_path, 'r')
    contents   = local_file.read()
    local_file.close()

    if not name: name = os.path.basename(local_path)
    core.sandbox.publish_api(contents, name = name)

def sandbox(f):
    @wraps(f)
    def wrapper(*a, **k):
        run_once()
        core.sandbox.execute(f.func_code)

    return wrapper
