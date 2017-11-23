# PyWally

An interactive P2P video wall SIP server.

If you're new to Python, don't panic and read [The Hitchhiker’s Guide to Python!](http://docs.python-guide.org/en/latest/).

## Setup

### Requirements
- Python ≥3.6

_If you want to manage and control your Python version accross projects, check out [pyenv](https://github.com/pyenv/pyenv)_

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
(venv) $ python run.py
```

By default, this will create a new server instance at http://localhost:8000.
The api can be accessed through the `/api` endpoint.

#### Documentation

The API system used allows for the automatic generation
of [Swagger](https://swagger.io/) specs, and running the
server creates a live documentation explorer, which can
be accessed at the endpoint `/api/doc`.
