from swagger_server.extensions.mongo_interface import MongoInterface
from swagger_server.models.public_profile import PublicProfile  # noqa: E501

def get_project_profile(project_id):  # noqa: E501
    """get a project owners public profile

    get a project owners public profile # noqa: E501

    :param project_id: ID of the project to lookup
    :type project_id: str

    :rtype: PublicProfile
    """

    m_interface = MongoInterface()
    results = m_interface.get_profile_by_public_project(project_id)
    if results is not None:
        return PublicProfile.from_dict(results)
    return {"error": "unable to lookup owner"}