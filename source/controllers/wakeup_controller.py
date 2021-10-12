import connexion
import six

from swagger_server import util


def wakeup():  # noqa: E501
    """wakeup the service

    this service needs to be woken up periodically to start running # noqa: E501


    :rtype: None
    """
    return {'status': 'awake'}
