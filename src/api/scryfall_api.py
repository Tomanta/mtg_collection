import requests
from ratelimit import limits, RateLimitException
from backoff import on_exception, expo

SCRYFALL_ROOT = "https://api.scryfall.com"
SCRYFALL_HEADERS = {
    "User-Agent": "MTG_Wishlist/1.0",
    "Accept": "*/*",
}

SCRYFALL_ENDPOINTS = {"bulk": "/bulk-data"}

ONE_SECOND = 1  # Scryfall requests only sending 10 request per second; we'll be nice and say 1 per second


@on_exception(expo, RateLimitException, max_tries=3)
@limits(calls=1, period=ONE_SECOND)
def call_api(endpoint: str) -> dict:
    if endpoint not in SCRYFALL_ENDPOINTS:
        raise ValueError()

    url = f"{SCRYFALL_ROOT}{SCRYFALL_ENDPOINTS[endpoint]}"
    response = requests.get(url, SCRYFALL_HEADERS)
    if response.status_code == 429:
        raise Exception("429: Fatal Error, Too many requests!")
    elif response.status_code == 404:
        raise Exception("404: Endpoint not found!")
    elif response.status_code != 200:
        raise Exception(f"API response {response.status_code}")

    return response.json()
