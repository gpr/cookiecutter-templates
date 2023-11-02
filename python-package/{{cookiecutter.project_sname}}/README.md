# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Quick Start

Install with pip (a recent version supporting poetry is required):

```
pip3 install --user -U pip
pip3 install --user git+{{cookiecutter.project_homepage}}.git#egg={{cookiecutter.project_slug}}
```

**NOTE**: `--user` install requires to have `~/.local/bin` in your path.

## Contributing

You must first install the system pre-requisites:

- poetry: dependencies manager

Then use poetry to create a new python3.9 based virtualenv in the project root dir (`.venv`):

```
git clone {{cookiecutter.project_homepage}}.git
cd {{cookiecutter.project_slug}}
poetry env use 3.12
poetry install --no-root
poetry shell  # or use `source .venv/bin/activate`
```

Finally setup pre-commit (in the virtualenv):

```
pre-commit install --install-hooks
```

See [Contribution Guide](CONTRIBUTING.md) for development rules.

## References

### Development tools

- https://python-poetry.org
- https://pre-commit.com
- https://docs.pytest.org/
- https://tox.readthedocs.io
- https://flake8.pycqa.org
- https://pylint.pycqa.org
- https://github.com/hadolint/hadolint
- https://direnv.net
