About
=====

This should show how to get Plex and nose working together.

Usage
=====

There is a Guardfile to run tests when files are saved to `Contents/Code` or `Contents/Tests`.

This should work without any modification on OS X. You need to get some env variables from the media server for Linux/Windows. [Visit /video/plex-nose-example/env](http://localhost:32400/video/plex-nose-example/env)

To run the tests manually, you need the env variables mentioned earlier:

    $ env ... python2.5 Contents/Tests/nose_runner.py Contents/Tests/test_....py

Caveats
=======

* Tests are run twice when using the Guardfile.
