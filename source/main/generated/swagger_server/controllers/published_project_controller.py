import connexion
import six

from swagger_server.models.project import Project  # noqa: E501
from swagger_server import util

from swagger_server.extensions.mongo_interface import MongoInterface


def get_connection_projects():  # noqa: E501
    """get published projects

     # noqa: E501


    :rtype: List[Project]
    """
    profile_id = connexion.request.authorization["profile_id"]
    m_interface = MongoInterface()
    res_count, results = m_interface.get_published_projects("connections", profile_id)
    resp_list = list()
    for res in results:
        resp_list.append(Project.from_dict(res))
    return resp_list

def get_public_projects():  # noqa: E501
    """get published projects

     # noqa: E501


    :rtype: List[Project]
    """
    profile_id = None
    if connexion.request.authorization is not None and "profile_id" in connexion.request.authorization:
        profile_id = connexion.request.authorization["profile_id"]
    m_interface = MongoInterface()
    res_count, results = m_interface.get_published_projects("public", profile_id)
    resp_list = list()
    for res in results:
        resp_list.append(Project.from_dict(res))
    return resp_list