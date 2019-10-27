# MTSR

This commandline tool will take a txt file with words and print the longest word and the longest word reversed.

## Assumptions

    Each line has only 1 word
    This program will be initiated from the console
    Words only contain language characters.
    File is in UTF-8 encoding or parsable in UTF-8 (ASCII)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Windows
```
python -m venv venv
. venv/bin/activate
pip install --requirement requirements.txt
python3 -m pip install -e .
mstr *FILENAME*
```

Linux
```
sudo apt-get install python3-venv
python3 -m venv venv
. venv/bin/activate
pip install --requirement requirements.txt
python3 -m pip install -e .
mtsr *FILENAME*
```

Example

Input:
test.txt
```
a
ab
abc
abcd
abcde
```
Console usage and output:
```
mtsr test.txt
abcde
edcba
```

### Prerequisites

This tool depends on the following to be setup.

- Python 3.7
- Pytest 5.0.1
- Pyfakefs 3.6.1

## Running the tests

We will create a new virtualenv here and run the tests


Windows
```
python -m venv venv
. venv/bin/activate
pip install --requirement requirements.txt
python3 -m pip install -e .
mtsr --help
python3 -m mtsr --help
python3 -m pytest -v
```

Linux
```
sudo apt-get install python3-venv
python3 -m venv venv
. venv/bin/activate
pip install --requirement requirements.txt
python3 -m pip install -e .
mtsr --help
python3 -m mtsr --help
python3 -m pytest -v
```

## Built With

* [Pytest](https://docs.pytest.org/en/latest/) - Test Framework
* [Python](https://python.org/) - Language

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Michael Alesso** - [mike-alesso](https://github.com/mike-alesso)
