## About

This should show how to get Plex and nose working together.

![example-output]

## Requirements

You are expected to have Plex Media Server installed, of course.

## Setup

This very repository is a functioning Gamespot.com channel.
Please feel free to clone and start hacking.

### Ubuntu

```bash
git clone git://github.com/mikew/plex-nose-example.git
cd plex-nose-example/
./run-ubuntu.sh Contents/Tests/test_....py # run specific tests
./run-ubuntu.sh Contents/Tests/ # run all tests
```

### OS X

```bash
git clone git://github.com/mikew/plex-nose-example.git
cd plex-nose-example/
./run-osx.sh Contents/Tests/test_....py # run specific tests
./run-osx.sh Contents/Tests/ # run all tests
```

### Other Operating Systems

To run the tests, you need to grab the environment variables that Plex
channels are run with. Install `plex-nose-example.bundle` as you would
any other Plex channel, [visit  /video/plex-nose-example/env][env-demo]
and note the contents of the `message` attribute. You are free to
shut down the server after this.

In addition to this, you must find the path to the media server's
`Framework.bundle/.../Versions/2/Python` and assign it to
`ENV[PLEX_FRAMEWORK_PATH]`

```bash
env PLEX_FRAMEWORK_PATH="..." ... python Contents/Tests/nose_runner.py /full/path/to/Contents/Tests/test_....py
```

Note the `/full/path/to/...` requirement.

### Integrating with existing channels

No modification to existing code is necessary, but you will need some files from this repository:

```
Contents/Libraries/Shared/nose/
Contents/Libraries/Shared/plex_nose.py
Contents/Libraries/Shared/spec.py
Contents/Tests/nose_runner.py
run-osx.sh
run-ubuntu.sh
```

## Writing Tests

[Nose][nose] is included and used to run the tests, so you can write
super-quick tests:

```python
import plex_nose

@plex_nose.sandbox
def test():
    ok_('some_data' not in Dict)
```

Just be sure to use the `plex_nose.sandbox` decorator.

Or, to make things even easier you can just extend `plex_nose.TestCase`
and stop using the decorator:

```python
import plex_nose

class TestMyChannel(plex_nose.TestCase):
    def test():
        ok_('some_data' not in Dict)
```

Note that the function definition is `def test():` and not `def test(self):`
as you would expect. This is due to the fact that different parts of
channel code are run in different sandboxes, there is no concept of `self`.

Either way, the tests are run in the exact\* environment as if they were
launched by the media server, but in a *fraction* of the time.

\* Well, not exact. The `Dict` is cleaned after each run, and the log file
is `./test.log` during the test runs.

### Helpers

As mentioned earlier, nose is included, so `eq_` and `ok_` are made
available to tests. In addition, there is also `eqL_`, `eqF_` and `eqcb_`.
These tests against localization keys and callbacks.

```python
class TestCaseHelpers(plex_unit.TestCase):
    def test_eqL():
        subject = L('some-key')
        eqL_(subject, 'some-key')
        # vs. eq_(subject._key, 'some-key')

    def test_eqF():
        subject = F('formatted-string', 'param')
        eqF_(subject, 'formatted-string')
        # vs. eq_(subject._key.string1._key, 'formatted-string')

    def test_eqcb():
        subject = DirectoryObject(key = Callback(Videos, section = 'all'))
        eqcb_(subject.key, Videos, section = 'all')
        # vs. eq_(subject.key, Callback(Videos, section = 'all'))
```

Code written in the tests won't have access to `file` or `open`, which is
necessary to mock data in tests some times. Use `plex_nose.publish_local_file`
in these situations.

```python
class TestPublishLocalFile(plex_nose.TestCase):
    @classmethod
    def setUpClass(cls):
        plex_nose.publish_local_file('Contents/Tests/all_videos.html',
            name = 'all_videos')

    def test():
        import mock
        mocked = HTML.ElementFromString(all_videos)
        @mock.patch.object(HTML, 'ElementFromURL', return_value = mocked)
        def test_inner(*a):
            subject = HTML.ElementFromURL(...)
            # TODO: write actual tests here
```

[Mock][mock] is located in `Contents/Libraries/Shared`, but not required to run
the tests.

## Guardfile

When using the Guardfile files saved to `Contents/Tests` will be
run automatically. Files saved to `Contents/Code` will also have the
corresponding test run, should one exist.

To get up and running with the Guardfile, all you need is ruby and
bundler installed.

### Ubuntu

```bash
sudo apt-get -y install ruby1.9.1 ruby1.9.1-dev
sudo gem install bundler rake
bundle install --path .bundle/gems/
bundle exec guard --clear -n f
```

### OS X

```bash
sudo gem install bundler
bundle install --path .bundle/gems/
bundle exec guard --clear -n f
```

[env-demo]: http://localhost:32400/video/plex-nose-example/env
[nose]: https://nose.readthedocs.org/en/latest/
[mock]: http://www.voidspace.org.uk/python/mock/
[example-output]: http://i.imgur.com/z2TWqix.png
