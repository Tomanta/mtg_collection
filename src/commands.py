import click


@click.command()
def bulk():
    click.echo("Hello!")
    SystemExit(0)  # Success
