import connexion
import time
import jwt
import os
from swagger_server.utilities import b2c_token_validator

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_BearerAuth(token):
    decoded_jwt = b2c_token_validator.extract_token(token)
    connexion.request.authorization = decoded_jwt
    return decoded_jwt