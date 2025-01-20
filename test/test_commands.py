from click.testing import CliRunner
import requests
import pytest
from commands import initial_load


class MockResponse:
    @staticmethod
    def response(*args):
        r = requests.Response()
        if args["url"].startswith("https://api.scryfall.com"):
            r.status_code = 200

            def json_func():
                return {"mock_key": "mock_response"}

            r.json = json_func
            return r

        r.status_code = 404
        return r


@pytest.mark.skip(reason="Disable until I figure out how to mock the API call")
def test_bulk(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(*args)

    monkeypatch.setattr(requests, "get", mock_get)

    runner = CliRunner()
    cli_result = runner.invoke(initial_load)
    assert cli_result.exit_code == 0
