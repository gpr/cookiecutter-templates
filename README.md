# Cookiecutter Templates

A collection of [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/index.html)
templates.

## Pre-requisites

You MUST set your personal Github access token in order to create the repo.

```shell
export GITHUB_ACCESS_TOKEN=your-token
```

See the file [.envrc.template](/.envrc.template) for a direnv template.

Then install all the pre-requisites:

```shell
pip install -r requirements.txt
```

or directly with _pipenv_:

```shell
pipenv install
```

## Quick Start

Example of usage (prefix the command with `pipenv run` if you use _pipenv_):

```shell
cookiecutter https://github.io/gpr/cookiecutter-templates.git --directory helm
```

Common options can bet set in `$HOME/.cookiecutterrc` config file:

```console
$ cat $HOME/.cookiecutterrc
default_context:
    author_name: "Gregory ROMÉ"
    author_email: "gpr@users.noreply.github.com"
    github_namespace: gpr
```
