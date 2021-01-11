import http.server as s
import click
from . import provider
from oauthlib.oauth2 import RequestValidator, WebApplicationServer


class MyRequestValidator(RequestValidator):
    pass


@click.group()
def cli():
    pass


@cli.command()
def server():
    print('serve')
    provider.app.run('0.0.0.0', port='8000', debug=True)


def main():
    server = WebApplicationServer(MyRequestValidator())
    print(server)
    cli()
