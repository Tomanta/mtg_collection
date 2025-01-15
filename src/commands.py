import click

@click.group()
def cli():
    pass

@click.command()
def bulk():
    click.echo(f"Hello!")
    SystemExit(0) # Success

cli.add_command(bulk)

if __name__ == '__main__':
    cli()