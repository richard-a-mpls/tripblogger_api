import requests
import os

class InvalidAuthorizationToken(Exception):
    def __init__(self, details):
        super().__init__('Invalid authorization token: ' + details)

def extract_token(token):
    my_headers={'Authorization': 'Bearer ' + os.environ.get('JWT_VALIDATE_AUTH'), 'tokenJwt': token}
    response = requests.get(os.environ.get('JWT_VALIDATE_ENDPOINT'),
                 headers=my_headers)
    if response.status_code != 200:
        raise InvalidAuthorizationToken("non 200 response")
    return response.json()