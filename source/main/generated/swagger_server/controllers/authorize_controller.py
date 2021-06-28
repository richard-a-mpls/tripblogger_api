import connexion
import six

from swagger_server.models.authorization_request import AuthorizationRequest  # noqa: E501
from swagger_server import util


def authorize(body):  # noqa: E501
    """authorize a session for token

    authorize based on a centralized token # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AuthorizationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
