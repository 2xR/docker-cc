import click

from . import commands


@click.group()
def cli():
    pass


for command in commands.all:
    cli.add_command(command)
