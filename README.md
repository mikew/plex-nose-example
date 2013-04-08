## About

This should show how to get Plex and nose working together.

## Requirements

You are expected to have Plex Media Server, of course.

## Usage

### Ubuntu

    git clone git://github.com/mikew/plex-nose-example.git
    cd plex-nose-example/
    ./run-ubuntu.sh Contents/Tests/test_....py # run specific tests
    ./run-ubuntu.sh Contents/Tests/ # run all tests

### OS X

    git clone git://github.com/mikew/plex-nose-example.git
    cd plex-nose-example/
    ./run-osx.sh Contents/Tests/test_....py # run specific tests
    ./run-osx.sh Contents/Tests/ # run all tests

### Other Operating Systems

To run the tests, you need to grab the environment variables that Plex
channels are run with. Install `plex-nose-example.bundle` as you would
any other Plex channel, [visit
/video/plex-nose-example/env](http://localhost:32400/video/plex-nose-example/env)
and note the contents of the `message` attribute.

In addition to this, you must find the path to the media server's
`Framework.bundle/.../Versions/2/Python` and assign it to `ENV[PLEX_FRAMEWORK_PATH]`

    $ env PLEX_FRAMEWORK_PATH="..." ... python Contents/Tests/nose_runner.py /full/path/to/Contents/Tests/test_....py

Note the `/full/path/to/...` requirement.

## Guardfile

When using the Guardfile files saved to `Contents/Tests` will be
run automatically. Files saved to `Contents/Code` will also have the
corresponding test run, should one exist.

To get up and running with the Guardfile, all you need is ruby and
bundler installed.

### Ubuntu

    sudo apt-get -y install
    sudo apt-get -y install ruby1.9.1 ruby1.9.1-dev
    sudo gem install bundler rake
    bundle install --path .bundle/gems/
    bundle exec guard --clear -n f

### OS X

    sudo gem install bundler
    bundle install --path .bundle/gems/
    bundle exec guard --clear -n f
