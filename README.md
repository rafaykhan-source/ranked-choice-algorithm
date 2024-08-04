# ranked-choice-matcher
An algorithm/automation program for matching people to events based on their ranked preferences.


## Configuration:

### Development Setup

In the `ranked-choice-matcher` directory, run:
```bash
./scripts/setup.sh
```

To setup the virtual environment, run:
```bash
python3 -m venv ~/.virtualenvs/ranked-choice
source ~/.virtualenvs/ranked-choice/bin/activate
pip install . && pip install .[development]
pre-commit install
```

## Usage:

Run the command below to see help menu / program usage.
```bash
python src/run.py -h
```

Run matches for a specified group.
```bash
python src/run.py instructors
```

## Acknowledgements
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)