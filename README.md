# widow-producer

A microservice implementation for sending data into a pub/sub system. Focus of project is on sending UCI data.

# Getting Started

## `poetry`

We use `poetry` to manage dependencies. You can setup `poetry` by following
instructions from [poetry's docs](https://python-poetry.org/docs/).

Then install packages to your environment:
```commandline
widow-producer git:(master) % python -m venv venv       # Setup virtual environment
widow-producer git:(master) % source venv/bin/activate  # Activate the created virtual environment
(venv) ➜  widow-producer git:(master) % poetry update   # Install/Update dependencies with poetry
```

### WARNING: Using `requirements.txt`

`requirements.txt` should be updated at regular intervals, 
but cannot be guaranteed to be up-to-date.

If you are contributing to this project, `poetry` is safer.

See [docs](./docs) for more information on contributing to this project.