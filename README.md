# About

This should show how to get Plex and nose working together.

# Requirements

You are expected to have Plex Media Server, of course.

Feel free to skip the ruby and bundler commands if you don't want to use
the Guardfile.

## Ubuntu

    sudo apt-get -y install ruby1.9.1 ruby1.9.1-dev
    sudo gem install bundler rake
    git clone git://github.com/mikew/plex-nose-example.git
    cd plex-nose-example/
    bundle install --path .bundle/gems/
    sudo bundle exec guard --clear -n f

## OS X

    sudo gem install bundler
    git clone git://github.com/mikew/plex-nose-example.git
    cd plex-nose-example/
    bundle install --path .bundle/gems/
    guard --clear -n f

# Usage

To run the tests, you need to grab the environment variables that Plex
channels are run with. [Visit
/video/plex-nose-example/env](http://localhost:32400/video/plex-nose-example/env)
and note the contents of the `message` attribute.

In addition to this, you must find the path to the media server's
`Framework.bundle/.../Versions/2/Python` and assign it to `ENV[PLEX_FRAMEWORK_PATH]`

    $ env PLEX_FRAMEWORK_PATH="..." ... python2.5 Contents/Tests/nose_runner.py Contents/Tests/test_....py

# Guardfile

Thankfully, all that noise earlier is consistent across OS X and Ubuntu
installs. When using the Guardfile files saved to `Contents/Tests` will be
run automatically. Files saved to `Contents/Code` will also have the
corresponding test run, should one exist.
