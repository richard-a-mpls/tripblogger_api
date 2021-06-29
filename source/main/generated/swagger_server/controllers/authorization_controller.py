from typing import List

from swagger_server.extensions.mongo_interface import MongoInterface
import connexion
import time

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_BearerAuth(token):

    # TODO - validation should be done via the mongo held api_token via m_interface.get_session_by_api_token
    m_interface = MongoInterface()
    api_session = m_interface.get_session_by_api_token(token)
    print ("response from check session was: " + str(api_session))
    if api_session is None:
        print ("Unable to find API Session by token")
        return None

    if int(time.time()) > api_session["api_token_expiration"]:
        print ("Api session has expired")
        # TODO - should remove the API session from mongo
        return None
    connexion.request.authorization = api_session
    return api_session


