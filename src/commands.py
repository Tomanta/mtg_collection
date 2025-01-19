import click
from database.db_setup import init_db
import data_commands

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
def data():
    """Data related commands"""
    pass


@setup.command(help="Initialize the database")
@click.option("--path", default=None, help="Path to the database file")
def create_db(path):
    if not path:
        path = ":memory:"
    # Check if path exists and is a directory, return error if not
    click.echo("Creating database...")
    init_db()


@data.command(help="Perform the initial load into the database")
def initial_load():
    data_commands.bulk()


def cmd_init():
    data.add_command(initial_load)
    setup.add_command(create_db)
    return cli
