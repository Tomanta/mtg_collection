import click
from database.db_setup import init_db
import data_commands
from database.db_conn import DBConn
from api.scryfall_api import call_api

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
def setup():
    """Setup options"""


@cli.group()
def search():
    """Search options"""


@cli.group()
def data():
    """Data related commands"""
    pass


@search.command(help="Perform a scryfall query")
@click.option("--query", help="The query parameters")
def scryfall_query(query):
    results = call_api("search", {"q": query, "unique": "art"})
    data_set = []
    for card in results["data"]:
        data_set.append((card["name"], " ".join([card["set"], card["collector_number"]])))
    for card in data_set:
        print(card)


@data.command(help="Load initial cards")
@click.option("--path", default=None, help="Path to the database file")
def load_cards(path):
    if not path:
        path = "sqlite:///:memory:"
    else:
        path = f"sqlite:///{path}"
    # Check if path exists and is a directory, return error if not
    db_conn = DBConn(path, echo=False)

    click.echo("Loading cards...")
    data_commands.load_all_cards(db_conn)


@setup.command(help="Initialize the database")
@click.option("--path", default=None, help="Path to the database file")
def create_db(path):
    if not path:
        path = "sqlite:///:memory:"
    else:
        path = f"sqlite:///{path}"
    # Check if path exists and is a directory, return error if not
    click.echo("Creating database...")
    init_db(connection_string=path)
    SystemExit(0)  # Success


@data.command(help="Perform the initial load into the database")
def initial_load():
    data_commands.bulk()
    SystemExit(0)  # Success


def cmd_init():
    data.add_command(initial_load)
    setup.add_command(create_db)
    return cli
