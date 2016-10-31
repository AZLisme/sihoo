# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

import pprint

import click

from sihoo import create_app
from sihoo.models import db

app = create_app()


@click.group()
def cli():
    pass


@click.command()
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=8080)
@click.option('--debug', default=True)
def start(host, port, debug):
    """Run the server"""
    click.echo("Starting the server...")
    from sihoo.ext.socketio import socketio
    socketio.run(app, host, port, debug=debug)


@click.command()
def show_config():
    """Display all the config parameters"""
    sep = "==========================================="
    print(sep)
    print("Flask Configuration")
    print("")
    pprint.pprint(app.config)
    print("")


@click.command()
def create_db():
    """Create database"""
    with app.app_context():
        db.create_all()


cli.add_command(start)
cli.add_command(show_config)
cli.add_command(create_db)

if __name__ == "__main__":
    cli()
