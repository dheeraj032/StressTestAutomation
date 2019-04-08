# StressTestAutomation

StressTestAutomation is a Python project for dealing with Android Stress testing using Monkey Scripting.

## Usage

```python
"Usage: python Monkey_Script.py Package_Name Throttle Verbose "
```

UI/Application Exerciser Monkey
The Monkey is a program that runs on your emulator or device and generates pseudo-random streams of user events such as clicks, touches, or gestures, as well as a number of system-level events. You can use the Monkey to stress-test applications that you are developing, in a random yet repeatable manner.

Overview
The Monkey is a command-line tool that you can run on any emulator instance or on a device. It sends a pseudo-random stream of user events into the system, which acts as a stress test on the application software you are developing.

The Monkey includes a number of options, but they break down into four primary categories:

Basic configuration options, such as setting the number of events to attempt.
Operational constraints, such as restricting the test to a single package.
Event types and frequencies.
Debugging options.

Basic use of the Monkey
You can launch the Monkey using a command line on your development machine or from a script. Because the Monkey runs in the emulator/device environment, you must launch it from a shell in that environment. You can do this by prefacing adb shell to each command, or by entering the shell and entering Monkey commands directly.

The basic syntax is:
```
$ adb shell monkey [options] <event-count>
```
With no options specified, the Monkey will launch in a quiet (non-verbose) mode, and will send events to any (and all) packages installed on your target. Here is a more typical command line, which will launch your application and send 500 pseudo-random events to it:
```
$ adb shell monkey -p your.package.name -v 500
```
## Project Structure
```
├── Reports
├── StressTest.egg-info
├── dist
├── src
│   ├── config
│   └── main
└── venv
    ├── bin
    ├── include
    │   └── python2.7 -> /System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7
    └── lib
        └── python2.7
            ├── config -> /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/config
            ├── distutils
            ├── encodings -> /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/encodings
            ├── lib-dynload -> /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload
            └── site-packages
                ├── pip
                │   ├── _internal
                │   │   ├── cli
                │   │   ├── commands
                │   │   ├── models
                │   │   ├── operations
                │   │   ├── req
                │   │   ├── utils
                │   │   └── vcs
                │   └── _vendor
                │       ├── cachecontrol
                │       │   └── caches
                │       ├── certifi
                │       ├── chardet
                │       │   └── cli
                │       ├── colorama
                │       ├── distlib
                │       │   └── _backport
                │       ├── html5lib
                │       │   ├── _trie
                │       │   ├── filters
                │       │   ├── treeadapters
                │       │   ├── treebuilders
                │       │   └── treewalkers
                │       ├── idna
                │       ├── lockfile
                │       ├── msgpack
                │       ├── packaging
                │       ├── pep517
                │       ├── pkg_resources
                │       ├── progress
                │       ├── pytoml
                │       ├── requests
                │       ├── urllib3
                │       │   ├── contrib
                │       │   │   └── _securetransport
                │       │   ├── packages
                │       │   │   ├── backports
                │       │   │   └── ssl_match_hostname
                │       │   └── util
                │       └── webencodings
                ├── pip-19.0.3.dist-info
                ├── pkg_resources
                │   ├── _vendor
                │   │   └── packaging
                │   └── extern
                ├── pp-1.6.5.dist-info
                ├── setuptools
                │   ├── _vendor
                │   │   └── packaging
                │   ├── command
                │   └── extern
                ├── setuptools-40.8.0.dist-info
                ├── uiautomator
                │   └── libs
                ├── uiautomator-0.3.6.dist-info
                ├── urllib3
                │   ├── contrib
                │   │   └── _securetransport
                │   ├── packages
                │   │   ├── backports
                │   │   └── ssl_match_hostname
                │   └── util
                ├── urllib3-1.24.1.dist-info
                ├── wheel
                │   └── cli
                └── wheel-0.33.1.dist-info

84 directories
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
