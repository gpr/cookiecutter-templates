# -*- coding: utf-8 -*-

import pytest
from click.testing import CliRunner


@pytest.fixture
def runner():
    return CliRunner()
