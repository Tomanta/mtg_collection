import json
from uuid import UUID
from database.db_setup import init_db
from database.db_conn import DBConn
from database.models import Card

sample_card = """
{
  "object": "card",
  "id": "56ebc372-aabd-4174-a943-c7bf59e5028d",
  "oracle_id": "e43e06fb-52b7-4f38-8fac-f31973b043f7",
  "multiverse_ids": [
    37113
  ],
  "mtgo_id": 17622,
  "mtgo_foil_id": 17623,
  "tcgplayer_id": 10190,
  "cardmarket_id": 2266,
  "name": "Phantom Nishoba",
  "lang": "en",
  "released_at": "2002-05-27",
  "uri": "https://api.scryfall.com/cards/56ebc372-aabd-4174-a943-c7bf59e5028d",
  "scryfall_uri": "https://scryfall.com/card/jud/140/phantom-nishoba?utm_source=api",
  "layout": "normal",
  "highres_image": true,
  "image_status": "highres_scan",
  "image_uris": {
    "small": "https://cards.scryfall.io/small/front/5/6/56ebc372-aabd-4174-a943-c7bf59e5028d.jpg?1562629953",
    "normal": "https://cards.scryfall.io/normal/front/5/6/56ebc372-aabd-4174-a943-c7bf59e5028d.jpg?1562629953",
    "large": "https://cards.scryfall.io/large/front/5/6/56ebc372-aabd-4174-a943-c7bf59e5028d.jpg?1562629953",
    "png": "https://cards.scryfall.io/png/front/5/6/56ebc372-aabd-4174-a943-c7bf59e5028d.png?1562629953",
    "art_crop": "https://cards.scryfall.io/art_crop/front/5/6/56ebc372-aabd-4174-a943-c7bf59e5028d.jpg?1562629953",
    "border_crop": "https://cards.scryfall.io/border_crop/front/5/6/56ebc372-aabd-4174-a943-c7bf59e5028d.jpg?1562629953"
  },
  "mana_cost": "{5}{G}{W}",
  "cmc": 7,
  "type_line": "Creature — Cat Beast Spirit",
  "oracle_text": "Trample\\nPhantom Nishoba enters with seven +1/+1 counters on it.\\nWhenever Phantom Nishoba deals damage, you gain that much life.\\nIf damage would be dealt to Phantom Nishoba, prevent that damage. Remove a +1/+1 counter from Phantom Nishoba.",
  "power": "0",
  "toughness": "0",
  "colors": [
    "G",
    "W"
  ],
  "color_identity": [
    "G",
    "W"
  ],
  "keywords": [
    "Trample"
  ],
  "legalities": {
    "standard": "not_legal",
    "future": "not_legal",
    "historic": "not_legal",
    "timeless": "not_legal",
    "gladiator": "not_legal",
    "pioneer": "not_legal",
    "explorer": "not_legal",
    "modern": "not_legal",
    "legacy": "legal",
    "pauper": "not_legal",
    "vintage": "legal",
    "penny": "not_legal",
    "commander": "legal",
    "oathbreaker": "legal",
    "standardbrawl": "not_legal",
    "brawl": "not_legal",
    "alchemy": "not_legal",
    "paupercommander": "not_legal",
    "duel": "legal",
    "oldschool": "not_legal",
    "premodern": "legal",
    "predh": "legal"
  },
  "games": [
    "paper",
    "mtgo"
  ],
  "reserved": false,
  "foil": true,
  "nonfoil": true,
  "finishes": [
    "nonfoil",
    "foil"
  ],
  "oversized": false,
  "promo": false,
  "reprint": false,
  "variation": false,
  "set_id": "cd82de1a-36fd-4618-bfe8-b45532a582d9",
  "set": "jud",
  "set_name": "Judgment",
  "set_type": "expansion",
  "set_uri": "https://api.scryfall.com/sets/cd82de1a-36fd-4618-bfe8-b45532a582d9",
  "set_search_uri": "https://api.scryfall.com/cards/search?order=set&q=e%3Ajud&unique=prints",
  "scryfall_set_uri": "https://scryfall.com/sets/jud?utm_source=api",
  "rulings_uri": "https://api.scryfall.com/cards/56ebc372-aabd-4174-a943-c7bf59e5028d/rulings",
  "prints_search_uri": "https://api.scryfall.com/cards/search?order=released&q=oracleid%3Ae43e06fb-52b7-4f38-8fac-f31973b043f7&unique=prints",
  "collector_number": "140",
  "digital": false,
  "rarity": "rare",
  "card_back_id": "0aeebaf5-8c7d-4636-9e82-8c27447861f7",
  "artist": "Arnie Swekel",
  "artist_ids": [
    "af10ecf2-eb82-4100-97b2-6c236b0fa644"
  ],
  "illustration_id": "2bdc53d2-1f4b-4f6d-b59d-985ff2a01268",
  "border_color": "black",
  "frame": "1997",
  "full_art": false,
  "textless": false,
  "booster": true,
  "story_spotlight": false,
  "edhrec_rank": 11036,
  "penny_rank": 4163,
  "prices": {
    "usd": "4.11",
    "usd_foil": "29.06",
    "usd_etched": null,
    "eur": "3.92",
    "eur_foil": "30.46",
    "tix": "0.49"
  },
  "related_uris": {
    "gatherer": "https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=37113&printed=false",
    "tcgplayer_infinite_articles": "https://partner.tcgplayer.com/c/4931599/1830156/21018?subId1=api&trafcat=infinite&u=https%3A%2F%2Finfinite.tcgplayer.com%2Fsearch%3FcontentMode%3Darticle%26game%3Dmagic%26partner%3Dscryfall%26q%3DPhantom%2BNishoba",
    "tcgplayer_infinite_decks": "https://partner.tcgplayer.com/c/4931599/1830156/21018?subId1=api&trafcat=infinite&u=https%3A%2F%2Finfinite.tcgplayer.com%2Fsearch%3FcontentMode%3Ddeck%26game%3Dmagic%26partner%3Dscryfall%26q%3DPhantom%2BNishoba",
    "edhrec": "https://edhrec.com/route/?cc=Phantom+Nishoba"
  },
  "purchase_uris": {
    "tcgplayer": "https://partner.tcgplayer.com/c/4931599/1830156/21018?subId1=api&u=https%3A%2F%2Fwww.tcgplayer.com%2Fproduct%2F10190%3Fpage%3D1",
    "cardmarket": "https://www.cardmarket.com/en/Magic/Products/Singles/Judgment/Phantom-Nishoba?referrer=scryfall&utm_campaign=card_prices&utm_medium=text&utm_source=scryfall",
    "cardhoarder": "https://www.cardhoarder.com/cards/17622?affiliate_id=scryfall&ref=card-profile&utm_campaign=affiliate&utm_medium=card&utm_source=scryfall"
  }
}
"""


def test_card_load():
    db_conn = DBConn()
    init_db(db_conn)
    card = json.loads(sample_card)

    # use .get() instead of [] here so it returns None if the key is not found
    new_card = Card(
        id=UUID(card.get("id")),
        arena_id=card.get("arena_id"),
        lang=card.get("lang"),
        tcgplayer_id=card.get("tcgplayer_id"),
        tcgplayer_etched_id=card.get("tcgplayer_etched_id"),
        cardmarket_id=card.get("cardmarked_it"),
        layout=card.get("layout"),
        oracle_id=UUID(card.get("oracle_id")) if card.get("oracle_id") else None,
        scryfall_uri=card.get("scryfall_uri"),
        uri=card.get("uri"),
        name=card.get("name"),
        set=card.get("set"),
        set_name=card.get("set_name"),
        rarity=card.get("rarity"),
        data=card,
    )
    print(new_card)
