# StressTestAutomation - Version 1.1

StressTestAutomation Framework is a one click Monkey test Android Automation using Python

## Package Structure 

```
StressTest/
├── Monkey_Script.py
├── Reports
│   ├── Error_log.txt
│   └── Event_logs.txt
├── StressTest.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
├── dist
│   └── StressTest-1.1.tar.gz
├── setup.py
├── src
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── config
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── constants.py
│   │   └── constants.pyc
│   └── main
│       ├── Call_Monkey.py
│       ├── Call_Monkey.pyc
│       ├── Check_adb.py
│       ├── Check_adb.pyc
│       ├── __init__.py
│       └── __init__.pyc

So on ..
73 directories, 935 files

```

## Usage

```
python Monkey_Script.py Package_Name Throttle Verbose
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
