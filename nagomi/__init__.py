import http.srever
from oauthlib.oauth2 import RequestValidator, WebApplicationServer


class MyRequestValidator(RequestValidator):
    pass

def main():
    server = WebApplicationServer(MyRequestValidator())
    print(server)