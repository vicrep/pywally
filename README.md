# PyWally

An interactive P2P video wall SIP server.

## Setup

### Development environment

- Install project in editable mode:
```bash
(venv) $ pip install -e .
```

- Install test & dev dependencies:
```bash
(venv) $ pip install -r requirements-tests.txt -r requirements-dev.txt
```

### Code audit / Linters

PyWally uses Pylama a code audit tool which runs various style & complexity check. Configure your editor to run against a single file each time it saves one.

- To run it globally:
```bash
(venv) $ pylama
```

- On a single path (file or directory):
```bash
(venv) $ pylama [path]
```

### Running tests

- Run tests:
```bash
(venv) $ py.test
```

- Run tests in auto reload (pytest-watch plugin):
```bash
(venv) $ ptw
```

### Running the server locally

```bash
(venv) $ flask run
```
or
```bash
(venv) $ python run.py
```
