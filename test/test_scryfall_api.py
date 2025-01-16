import requests
import requests_mock
from api.scryfall_api import call_api

adapter = requests_mock.Adapter()

adapter.register_uri('GET', 'https://api.scryfall.com/bulk-data', request_headers={}, status_code = 200, text='{"bob":"dole"}')

def test_bulk_api():
    expected = {"test":"success"}

    with requests_mock.Mocker() as m:
        result = call_api("bulk")
    assert result == expected
