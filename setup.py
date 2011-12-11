import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='html5writer',
    version='0.1',
    author='Bradley Wright <brad@intranation.com>',
    packages=['html5writer', 'tests'],
    keywords = "rst html5 doctutils",
    description='A reStructuredText writer for writing semantic HTML5',
    long_description=read('README.rst'),
    license='BSD License',
    include_package_data=True,
    install_requires=['docutils']
)
