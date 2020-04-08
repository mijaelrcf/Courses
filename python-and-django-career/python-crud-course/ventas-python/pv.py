import click

from clients import commands as clients_commands

CLIENTS_TABLE = 'clients.csv'


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {} 
    ctx.obj['clients_table'] = CLIENTS_TABLE


cli.add_command(clients_commands.all)

# commands to install on windows
# virtualenv --python=python3 venv
# venv\scripts\activate
# pip install --editable
# where pv
# pv --help
# pv clients --help