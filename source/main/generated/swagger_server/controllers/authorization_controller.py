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

def check_OptionalBearerAuth(token):
    # in this case, it's ok if the user isn't authenticated, but if they are
    # we need to knwo who they are.
    try:
        decoded_jwt = jwt.decode(token, os.environ["jwt_secret"], algorithms=["HS256"])
        if int(time.time()) > decoded_jwt["expires"]:
            print ("JWT has expired")
            return None
        connexion.request.authorization = decoded_jwt
        return decoded_jwt
    except:
        print ("user not authenticated which is ok")
        return {}
