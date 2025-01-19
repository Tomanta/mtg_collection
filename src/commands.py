import click
from pathlib import Path
from api.scryfall_api import call_api
from database.db_setup import init_db
import requests

"""
Need:
- setup commands
    - initial DB creation
    - destroy DB (maybe add safeguard)
- data update commands:
    - initial load from bulk
    - refresh from bulk
    - specific card update, by ID or name
    - image download
    - refresh prices (single card or pass in list)
        - could run off cron job
- query commands:
    - Scryfall-style query
    - look up specific card or basic characteristic searches
- collection/wishlist management
    - view [all or by group]
    - add
    - update status (owned/need)
    - remove
    - export (format)
- launch textual interface
- launch gui interface
"""

@click.group()
def cli() -> None:
    pass

@cli.group()
def db():
    """Database group"""
    pass


def file_download(source, destination):
    response = requests.get(source)
    if response.status_code == 200:
        with open(destination, "wb") as f:
            f.write(response.content)

        return True  # File saved successfully

    return False  # File failed

@db.command()
def create():
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


def cmd_init():
    cli.add_command(bulk)
    db.add_command(create)
    return cli
