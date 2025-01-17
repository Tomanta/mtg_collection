import requests
import requests_mock
import json
from api.scryfall_api import call_api
import pytest

bulk_response = """
{
  "object": "list",
  "has_more": false,
  "data": [
    {
      "object": "bulk_data",
      "id": "27bf3214-1271-490b-bdfe-c0be6c23d02e",
      "type": "oracle_cards",
      "updated_at": "2025-01-16T22:05:35.071+00:00",
      "uri": "https://api.scryfall.com/bulk-data/27bf3214-1271-490b-bdfe-c0be6c23d02e",
      "name": "Oracle Cards",
      "description": "A JSON file containing one Scryfall card object for each Oracle ID on Scryfall. The chosen sets for the cards are an attempt to return the most up-to-date recognizable version of the card.",
      "size": 155539753,
      "download_uri": "https://data.scryfall.io/oracle-cards/oracle-cards-20250116220535.json",
      "content_type": "application/json",
      "content_encoding": "gzip"
    },
    {
      "object": "bulk_data",
      "id": "6bbcf976-6369-4401-88fc-3a9e4984c305",
      "type": "unique_artwork",
      "updated_at": "2025-01-16T22:21:48.122+00:00",
      "uri": "https://api.scryfall.com/bulk-data/6bbcf976-6369-4401-88fc-3a9e4984c305",
      "name": "Unique Artwork",
      "description": "A JSON file of Scryfall card objects that together contain all unique artworks. The chosen cards promote the best image scans.",
      "size": 217146968,
      "download_uri": "https://data.scryfall.io/unique-artwork/unique-artwork-20250116222148.json",
      "content_type": "application/json",
      "content_encoding": "gzip"
    },
    {
      "object": "bulk_data",
      "id": "e2ef41e3-5778-4bc2-af3f-78eca4dd9c23",
      "type": "default_cards",
      "updated_at": "2025-01-16T22:39:59.251+00:00",
      "uri": "https://api.scryfall.com/bulk-data/e2ef41e3-5778-4bc2-af3f-78eca4dd9c23",
      "name": "Default Cards",
      "description": "A JSON file containing every card object on Scryfall in English or the printed language if the card is only available in one language.",
      "size": 484181553,
      "download_uri": "https://data.scryfall.io/default-cards/default-cards-20250116223959.json",
      "content_type": "application/json",
      "content_encoding": "gzip"
    },
    {
      "object": "bulk_data",
      "id": "922288cb-4bef-45e1-bb30-0c2bd3d3534f",
      "type": "all_cards",
      "updated_at": "2025-01-16T10:21:09.648+00:00",
      "uri": "https://api.scryfall.com/bulk-data/922288cb-4bef-45e1-bb30-0c2bd3d3534f",
      "name": "All Cards",
      "description": "A JSON file containing every card object on Scryfall in every language.",
      "size": 2312117508,
      "download_uri": "https://data.scryfall.io/all-cards/all-cards-20250116102109.json",
      "content_type": "application/json",
      "content_encoding": "gzip"
    },
    {
      "object": "bulk_data",
      "id": "06f54c0b-ab9c-452d-b35a-8297db5eb940",
      "type": "rulings",
      "updated_at": "2025-01-16T22:00:37.146+00:00",
      "uri": "https://api.scryfall.com/bulk-data/06f54c0b-ab9c-452d-b35a-8297db5eb940",
      "name": "Rulings",
      "description": "A JSON file containing all Rulings on Scryfall. Each ruling refers to cards via an `oracle_id`.",
      "size": 22936346,
      "download_uri": "https://data.scryfall.io/rulings/rulings-20250116220037.json",
      "content_type": "application/json",
      "content_encoding": "gzip"
    }
  ]
}
"""

def test_bulk_api_success():
    expected = json.loads(bulk_response)

    with requests_mock.Mocker() as m:
        m.get('https://api.scryfall.com/bulk-data', status_code = 200, text = bulk_response)
        result = call_api("bulk")
    assert result == expected


def test_bulk_api_404():
    with requests_mock.Mocker() as m:
        m.get('https://api.scryfall.com/bulk-data', status_code = 404)
        with pytest.raises(ValueError):
            result = call_api("bob")
    