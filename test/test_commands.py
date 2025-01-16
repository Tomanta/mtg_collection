from click.testing import CliRunner
import requests
import pytest
from commands import bulk


class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


@pytest.mark.skip(reason="Disable until I figure out how to mock the API call")
def test_bulk(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    runner = CliRunner()
    result = runner.invoke(bulk)
    assert result.exit_code == 0
