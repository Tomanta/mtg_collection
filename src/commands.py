import click
from api.scryfall_api import call_api


@click.command()
def bulk():
    click.echo("Hello!")
    call_api("bulk")
    SystemExit(0)  # Success
