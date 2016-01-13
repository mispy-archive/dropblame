dropblame
=========

.. image:: https://badge.fury.io/py/dropblame.svg
    :target: https://badge.fury.io/py/dropblame

|
A Python command line tool which will convert the revision history of a
Dropbox file into a git repository, so you can run ``git blame`` or
``git diff``. Suggested by `@cgranade <https://twitter.com/cgranade/status/683957037173059584>`_.

Installation
------------

``pip install dropblame``

Usage
-----

``drop blame /path/to/Dropbox/file``

Syncs Dropbox revisions to a git repo and runs git blame. Any additional
arguments will be passed to git blame.

``drop cd /path/to/Dropbox/file``

Syncs Dropbox revisions to a git repo and then opens a shell there, if
you want to run diff or other operations. The commit messages contain
Dropbox revision ids.

Notes
-----

The first time you run ``drop`` you will be asked for configuration
details to connect to Dropbox, which will be stored in
~/.dropblame/config.yml.

Note that this tool can only go back as far as the Dropbox API will
allow, which is currently 100 revisions.

I've only tested this on Linux so far.
