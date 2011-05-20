from os import path, chdir
from setuptools import setup
version = __import__('nose_timer').__version__

packages, data_files = [], []
root_dir = path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)

setup(
    name='nose-timer',
    version=version,
    description="A python nose plugin to time tests.",
    long_description="This plugin provides test timings to identify which tests might be taking the most. From this information, it might be useful to couple individual tests nose's `--with-profile` option to profile problematic tests.",
    author='Mahmoud Abdelkader',
    author_email='',
    url='https://github.com/patjenk/nose-timer',
    install_requires=[
        'nose==1.0.0',
    ],
    setup_requires=[],
    packages=packages,
    include_package_data=True,
    test_suite='nose.collector',
    zip_safe=False,
    py_modules=['nose_timer'],
    entry_points={
        'nose.plugins.0.10': [
            'nose_timer = nose_timer.NoseTimer',
        ]
    },
)
