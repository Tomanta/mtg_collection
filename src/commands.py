import click
import os
from pathlib import Path
from api.scryfall_api import call_api
from database.db_setup import init_db
import requests


def file_download(source, destination):
    response = requests.get(source)
    if response.status_code == 200:
        with open(destination, "wb") as f:
            f.write(response.content)

        return True  # File saved successfully

    return False  # File failed

@click.command()
def create_db():
    click.echo("Creating database...")
    init_db()

@click.command()
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
