import connexion
import six
from swagger_server.extensions.mongo_interface import MongoInterface
from swagger_server.models.profile import Profile  # noqa: E501
from swagger_server import util


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
    return 'do some magic!'


def get_session_profile():  # noqa: E501
    """get a profile based on authorized session

     # noqa: E501


    :rtype: Profile
    """
    print("look at profiles for user: " + str(connexion.request.authorization))
    print("found profile: " + str(connexion.request.authorization["profile"]))
    response = Profile.from_dict(connexion.request.authorization["profile"])
    return response
