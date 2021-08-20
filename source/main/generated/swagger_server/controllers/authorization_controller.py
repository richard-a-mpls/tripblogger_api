import connexion
import time
import jwt
import os

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_BearerAuth(token):

    # TODO - validation should be done via the mongo held api_token via m_interface.get_session_by_api_token
    decoded_jwt = jwt.decode(token, os.environ["jwt_secret"], algorithms=["HS256"])
    if int(time.time()) > decoded_jwt["expires"]:
        print ("JWT has expired")
        ## TODO - should remove the API session from mongo
        return None
    connexion.request.authorization = decoded_jwt
    return decoded_jwt


