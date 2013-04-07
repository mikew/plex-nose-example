# About

This should show how to get Plex and nose working together.

# Requirements

You are expected to have Plex Media Server and nose installed, of
course. But be certain to install nose for the python version used by
the media server.

Feel free to skip the ruby and bundler commands if you don't want to use
the Guardfile.

## Ubuntu

    sudo pip install nose
    sudo apt-get -y install ruby1.9.1 ruby1.9.1-dev
    sudo gem install bundler rake
    git clone git://github.com/mikew/plex-nose-example.git
    cd plex-nose-example/
    bundle install --path .bundle/gems/
    guard --clear -n f

## OS X

    sudo easy_install2.5 nose
    sudo gem install bundler
    cd plex-nose-example/
    bundle install --path .bundle/gems/
    guard --clear -n f

# Usage

To run the tests, you need the env :

    $ env ... python2.5 Contents/Tests/nose_runner.py Contents/Tests/test_....py
