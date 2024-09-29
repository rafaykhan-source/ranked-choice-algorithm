# ranked-choice-matcher
Matches people to events based on their ranked preferences.

## Configuration:

### Development Setup

In the `ranked-choice-matcher` directory, run:
```bash
mkdir build data results events
```

To setup the virtual environment, run:
```bash
uv sync
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

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)