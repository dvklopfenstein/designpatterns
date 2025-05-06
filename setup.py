"""For building and installing TimeTracker"""

__copyright__ = 'Copyright (C) 2025-present, DV Klopfenstein, PhD. All rights reserved'
__author__ = "DV Klopfenstein, PhD"


from os.path import join
from os.path import abspath
from os.path import dirname
from setuptools import setup

PACKAGES = [
    'examples.designpatterns',
    'examples.designpatterns.simplefactory',
]

PACKAGE_DIRS = {p:join(*p.split('.')) for p in PACKAGES}

def get_long_description():
    """Return the contents of the README.md as a string"""
    dir_cur = abspath(dirname(__file__))
    with open(join(dir_cur, 'README.md'), 'rb') as ifstrm:
        return ifstrm.read().decode("UTF-8")

CONSOLE_SCRIPTS = [
    'simplefactory=examples.designpatterns.simplefactory.doorfactory:main',
    'access=examples.accessmodifiers:main',
]



setup(
    # The name of the project on PyPi
    name='designpatterns',
    # https://peps.python.org/pep-0440/
    version='0.0.1',
    author='DV Klopfenstein, PhD',
    author_email='dvklopfenstein@protonmail.com',
    packages=PACKAGES,
    package_dir=PACKAGE_DIRS,
    entry_points={
        'console_scripts': CONSOLE_SCRIPTS,
    },
    # https://pypi.org/classifiers/
    classifiers=[
        'Programming Language :: Python',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
    url='http://github.com/dvklopfenstein/timetracking',
    description="A lightweight, repo-based, command-line designpatterns "
                "that stores data in csv files",
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
)

# Copyright (C) 2025-present, DV Klopfenstein, PhD. All rights reserved
