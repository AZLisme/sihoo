# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from sihoo import make_flask_app
import click
import pprint

flask_app = make_flask_app()


@click.group()
def cli():
    pass


@click.command()
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=8080)
@click.option('--debug', default=True)
def start(host, port, debug):
    """Run the server"""
    click.echo("Start the server")
    flask_app.run(host=host, port=port, debug=debug)


@click.command()
def showConfig():
    """Display all the config parameters"""
    pprint.pprint(flask_app.config)


cli.add_command(start)
cli.add_command(showConfig)


if __name__ == "__main__":
    cli()
