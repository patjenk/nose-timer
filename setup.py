from os import path, chdir
from setuptools import setup
VERSION = (0,1,'pre')

# Dynamically calculate the version based on VERSION tuple
if len(VERSION) > 2 and VERSION[2] is not None:
    str_version = "%s.%s_%s" % VERSION[:3]
else:
    str_version = "%s.%s" % VERSION[:2]

version = str_version

setup(
    name='nose-timer',
    version=version,
    description="A python nose plugin to time tests.",
    long_description="This plugin provides test timings to identify which tests might be taking the most. From this information, it might be useful to couple individual tests nose's `--with-profile` option to profile problematic tests.",
    author='Mahmoud Abdelkader',
    author_email='',
    url='https://github.com/patjenk/nose-timer',
    install_requires=[
        'nose>1.0.0,<1.1.3',
    ],
    setup_requires=[],
    test_suite='nose.collector',
    zip_safe=False,
    py_modules=['nose_timer'],
    entry_points={
        'nose.plugins.0.10': [
            'nose_timer = nose_timer:NoseTimer',
        ]
    },
)
