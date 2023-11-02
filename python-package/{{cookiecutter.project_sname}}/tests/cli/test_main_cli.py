# -*- coding: utf-8 -*-

from {{cookiecutter.project_slug}}.cli.main_cli import main_cli


def test_main_cli(runner):
    """Test mani cli."""

    response = runner.invoke(main_cli, [])
    assert response.exit_code == 0
    assert "Hello world!" in response.output
