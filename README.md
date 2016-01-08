# dropblame

A Python command line tool which will take revisions of a Dropbox file in a shared folder and run `git blame` on them. Suggested by [@cgranade](https://twitter.com/cgranade/status/683957037173059584).

## Dependencies

`pip install dropbox pyyaml ndg-httpsclient`

You will need git-- this doesn't reimplement git blame, it just takes all the revs and sticks them into a temporary git repo.

`drop` itself is a standalone Python script; you can put it somewhere on your PATH, if you like!

## Usage

`drop blame /path/to/Dropbox/file`

Any additional arguments will be passed to git blame. First time you run this you will be asked for configuration details to connect to Dropbox, which will be stored in ~/.dropblame/config.yml.
