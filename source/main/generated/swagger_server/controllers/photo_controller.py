import connexion
import six
from swagger_server.extensions.mongo_interface import MongoInterface
from flask import send_file
import io

from swagger_server import util


def get_photo(photo_id):  # noqa: E501
    """get a photo

     # noqa: E501

    :param photo_id: ID of the photo to return
    :type photo_id: str

    :rtype: None
    """
    m_interface = MongoInterface()
    photo = m_interface.get_photo(photo_id)
    print (photo)

    print (photo["name"])
    obj = photo["data"]
    print (obj)
    return send_file(io.BytesIO(obj), mimetype='image/jpeg')
    #return 'do some magic!'
