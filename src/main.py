import click
from commands import bulk


@click.group()
def cli():
    pass


if __name__ == "__main__":
    cli.add_command(bulk)
    cli()
