import connexion
import six
from swagger_server.extensions.mongo_interface import MongoInterface
from flask import send_file, request
import io
from swagger_server.models.photo import Photo
from swagger_server import util
from bson.binary import Binary
import imghdr


def add_photo(order_id=None, user_id=None, file_name=None):  # noqa: E501
    """upload a photo

    upload a photo # noqa: E501

    :param order_id:
    :type order_id: int
    :param user_id:
    :type user_id: int
    :param file_name:
    :type file_name: strstr

    :rtype: None
    """
    print (connexion.request)
    print (connexion.request.files)
    for f in connexion.request.files:
        print ("one")
        print (f)

    print (connexion.request.files['file'])
    uploaded_file = connexion.request.files['file']
    print (uploaded_file.filename)

    header = uploaded_file.stream.read(512)
    uploaded_file.stream.seek(0)

    photo = Photo()
    photo.name = uploaded_file.filename
    photo.type = imghdr.what(None, header)

    print (imghdr.what(None, header))

    photo.data = Binary(uploaded_file.stream.read())
    m_interface = MongoInterface()
    inserted_id = m_interface.create_photo(photo.to_dict())
    #TODO, define proper return object and refactor.
    return {'id': inserted_id}


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
