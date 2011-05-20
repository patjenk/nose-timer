# A plugin for python nose tests that provides runtimes for tests

## nose-timer

This plugin provides test timings to identify which tests might be taking the most time. From this information, it might be useful to couple individual tests nose's `--with-profile` option to profile problematic tests.

## Background

@mahmoudimus wrote this timer for nose tests and I want to use it in my projects. So, I'm creating a repository so I can install it with PIP. The original gist can be viewed in all it's glory at https://gist.github.com/848183.

## Install

`pip install -e git+git://github.com/patjenk/nose-timer.git#egg=nose-timer`

## Usage

The --with-test-timers can be passed to nose tests and after all the tests are excuted, they will be printed out with their runtimes in ascending order. 
