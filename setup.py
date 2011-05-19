from setuptools import setup
version = __import__('nose-timer').__version__

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
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
        'werkzeug>=0.6.2',
        'mako>=0.3.6',
        'simplejson',
        'mock',
        'nose==1.0.0',
        'boto>=2.0a2',
        'SQLAlchemy>=0.6.3',
    ],
    setup_requires=[],
    packages=packages,
    include_package_data=True,
    test_suite='nose.collector',
    zip_safe=False,
    entry_points={
        'nose.plugins.0.10': [
            'with-test-timers = application.utils.test_timer:TestTimer',
        ]
    },
)
