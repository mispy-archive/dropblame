# dropblame

A Python tool which will take revisions of a Dropbox file in a shared folder and run `git blame` on them.

## Dependencies

`pip install dropbox pyyaml ndg-httpsclient`

## Usage

`drop blame /path/to/Dropbox/file`

Any additional arguments will be passed to git blame. First time you run this you will be asked for configuration details to connect to Dropbox, which will be stored in ~/.dropblame/config.
