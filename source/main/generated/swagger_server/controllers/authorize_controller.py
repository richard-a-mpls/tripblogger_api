import connexion
import six

from swagger_server.models.authorization_request import AuthorizationRequest  # noqa: E501
from swagger_server.extensions.authorization_extensions import AuthorizationExtensions
from swagger_server import util


def authorize(body):  # noqa: E501
    print ("AUTHORIZE")
    """authorize a session for token

    authorize based on a centralized token # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AuthorizationRequest.from_dict(connexion.request.get_json())  # noqa: E501

    print("let's do AE")
    ae = AuthorizationExtensions()
    print ("back from AE")
    api_token = ae.process_authentication("fb", body.identity_token)
    print ("Api Token: " + api_token)

    return {"api_token": api_token}
