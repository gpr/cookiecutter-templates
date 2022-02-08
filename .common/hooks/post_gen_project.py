#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import git
from github import Github
from github.GithubObject import NotSet


def create_github_project(config):
    """Create GitHub repository"""
    token = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    if token is None:
        raise Exception("fatal: you must set GITHUB_ACCESS_TOKEN")

    # using an access token
    client = Github(token)
    user = client.get_user()

    repo = user.create_repo(
        config.get("name"),
        description=config.get("description"),
        homepage=config.get("homepage"),
        private=config.get("private", True),
        has_issues=config.get("has_issues", True),
        has_wiki=config.get("has_wiki", False),
        has_downloads=config.get("has_downloads", True),
        has_projects=config.get("has_projects", False),
        auto_init=config.get("auto_init", False),
        license_template=config.get("license_template", NotSet),
        gitignore_template=config.get("gitignore_template", NotSet),
        allow_squash_merge=config.get("allow_squash_merge", False),
        allow_merge_commit=config.get("allow_merge_commit", True),
        allow_rebase_merge=config.get("allow_rebase_merge", True),
        delete_branch_on_merge=config.get("delete_branch_on_merge", True),
    )

    return repo


def yesno_to_int(s):
    """Convert yes/no answer to 1/0"""
    if s == "y" or s == "yes":
        return 1
    return 0


def yesno_to_bool(s):
    """Convert yes/no answer to True/False"""
    if s == "y" or s == "yes":
        return True
    return False


def git_init():
    """Init local git repository"""
    repo = git.Repo.init(os.path.realpath(os.path.curdir))

    if len(repo.remotes) == 1:
        action_msg = "update"
        origin = repo.remotes[0]
    else:
        action_msg = "create"
        origin = repo.create_remote(
            "origin",
            "ssh://git@github.com:{{ cookiecutter.github_namespace }}/{{ cookiecutter.project_slug }}.git",
        )

    repo.config_writer().set_value(
        "user", "name", "{{ cookiecutter.author_name }}"
    ).release()
    repo.config_writer().set_value(
        "user", "email", "{{ cookiecutter.author_email }}"
    ).release()
    repo.git.add(A=True)
    repo.index.commit("auto(cookiecutter): {} project".format(action_msg))

    main = repo.create_head("main")
    repo.head.reference = main

    if "{{ cookiecutter.git_push }}" == "y":
        origin.push("main:main")


if __name__ == "__main__":
    config = {
        "name": "{{ cookiecutter.project_slug }}",
        "description": "{{ cookiecutter.project_description }}",
        "homepage": "{{ cookiecutter.project_homepage }}",
        "private": yesno_to_bool("{{ cookiecutter.github_private }}"),
    }

    github_project = None

    if "{{ cookiecutter.create_github_project }}" == "y":
        github_project = create_github_project(config)
        print("Github project {} created!".format(github_project.id))

    git_init()

    os.system("pre-commit install --install-hooks")
    os.system("cp .envrc.template .envrc")
