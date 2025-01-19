import click
from commands import bulk, create_db


@click.group()
def cli():
    pass


if __name__ == "__main__":
    cli.add_command(bulk)
    cli.add_command(create_db)
    cli()
