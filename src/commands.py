import click
from api.scryfall_api import call_api


@click.command()
def bulk():
    click.echo("Hello!")
    call_api("bulk")

    # Call the bulk API
    # Check if we already have the current version of whatever data we care about (make sub commands?)
    # If not, download that object

    SystemExit(0)  # Success
