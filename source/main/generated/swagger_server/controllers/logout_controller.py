import connexion
import six

from swagger_server import util
from swagger_server.extensions.mongo_interface import MongoInterface

def logout(api_token):  # noqa: E501
    """de-authorize a session for token

    de-authorize a session for token # noqa: E501

    :param api_token: api token to delete
    :type api_token: str

    :rtype: None
    """
    m_interface = MongoInterface()
    m_interface.delete_session_by_api_token(api_token)
    return {"logout": "success"}
