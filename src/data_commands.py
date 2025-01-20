import click
import json
import requests
from pathlib import Path
from sqlalchemy.orm import Session
from uuid import UUID
from database.models import Card
from api.scryfall_api import call_api


def load_all_cards(dbconn):
    bulk = "data/e2ef41e3-5778-4bc2-af3f-78eca4dd9c23.json"

    engine = dbconn.get_engine()

    with open(bulk, "r") as f:
        card_data = json.load(f)

    with Session(engine) as session:
        for card in card_data:
            click.echo(f"Loading {card.get('name')}")
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
            session.add(new_card)
        session.commit()

    SystemExit(0)  # Success


def file_download(source, destination):
    response = requests.get(source)
    if response.status_code == 200:
        with open(destination, "wb") as f:
            f.write(response.content)

        return True  # File saved successfully

    return False  # File failed


def bulk():
    bulk_data = call_api("bulk")

    directory = {}

    for item in bulk_data["data"]:
        directory[item["type"]] = {
            "download_uri": item["download_uri"],
            "filename": f"{item['id']}.json",
            "updated_at": item["updated_at"],
        }

    base_path = Path.cwd()
    bulk_path = Path("data")
    file = Path(directory["default_cards"]["filename"])
    full_path = base_path / bulk_path / file
    print(full_path)

    if full_path.is_file():
        click.echo("File already exists!")
    else:
        result = file_download(directory["default_cards"]["download_uri"], full_path)
        if result:
            click.echo("File downloaded successfully")
        else:
            click.echo("File download failed")

    SystemExit(0)  # Success
