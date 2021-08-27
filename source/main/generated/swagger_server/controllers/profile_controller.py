import connexion
import six
from swagger_server.extensions.mongo_interface import MongoInterface
from swagger_server.models.profile import Profile  # noqa: E501

profile_attributes = ["profile_name"]

def add_profile(body):  # noqa: E501
    """create a profile

    create a profile # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Profile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_profile(profile_id):  # noqa: E501
    """get a profile by id

    get that profile # noqa: E501

    :param profile_id: ID of profile to return
    :type profile_id: str

    :rtype: Profile
    """
    m_interface = MongoInterface()
    return m_interface.get_profile_by_id(profile_id)
    return 'do some magic!'


def get_session_profile():  # noqa: E501
    """get a profile based on authorized session

     # noqa: E501


    :rtype: Profile
    """
    response = get_profile(connexion.request.authorization["profile_id"])
    return_profile = Profile.from_dict(response)
    return return_profile


def patch_profile(body, profile_id):  # noqa: E501
    """update attributes of a profile

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param profile_id: ID of profile to return
    :type profile_id: str

    :rtype: Profile
    """
    authenticated_id = connexion.request.authorization["profile_id"]
    if authenticated_id != profile_id:
        return {
            "detail": "Not authorized to modify this object",
            "status": "401",
            "title": "Unauthorized",
            "type": "about:blank"
        }

    if connexion.request.is_json:
        body = Profile.from_dict(connexion.request.get_json())  # noqa: E501

    set_values = {}
    persist_changes = False
    if body.profile_name is not None:
        set_values['profile_name'] = body.profile_name
        persist_changes = True

    if body.profile_img is not None:
        set_values['profile_img'] = body.profile_img
        persist_changes = True


    if persist_changes:
        m_interface = MongoInterface()
        m_interface.patch_profile(profile_id, set_values)

    return get_session_profile()
