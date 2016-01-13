# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dropblame',
    packages=['dropblame'],
    version='0.0.1',
    description='"git blame" for Dropbox files',
    long_description=long_description,
    author='Jaiden Mispy',
    author_email='jaiden@mispy.me',
    url='https://github.com/mispy/dropblame',
    keywords='git dropbox command-line',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ],
    install_requires=['dropbox', 'pyyaml', 'ndg-httpsclient'],
    entry_points={
        'console_scripts': [
            'drop=dropblame:main',
        ],
    },
)
