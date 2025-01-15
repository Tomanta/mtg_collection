import pytest
from click.testing import CliRunner
from commands import bulk


def test_bulk():
    runner = CliRunner()
    result = runner.invoke(bulk)
    assert result.exit_code == 0
    assert result.output == "Hello!\n"