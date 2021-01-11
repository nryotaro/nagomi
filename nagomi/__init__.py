import http.server as s
import click
from oauthlib.oauth2 import RequestValidator, WebApplicationServer


class MyRequestValidator(RequestValidator):
    pass


@click.group()
def cli():
    pass

@cli.command()
def server():
    print('serve')

def main():
    server = WebApplicationServer(MyRequestValidator())
    print(server)
    cli()