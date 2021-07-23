import connexion
import six
from swagger_server.extensions.mongo_interface import MongoInterface
from flask import send_file, request
import io
from swagger_server.models.photo import Photo
from swagger_server import util
from bson.binary import Binary
import imghdr

from PIL import Image
import math


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
    uploaded_file = connexion.request.files['file']

    header = uploaded_file.stream.read(512)
    uploaded_file.stream.seek(0)

    photo = Photo()
    photo.name = uploaded_file.filename
    photo.type = imghdr.what(None, header)

    img = Image.open(uploaded_file.stream)
    x, y = img.size
    x2, y2 = math.floor(x / 4), math.floor(y / 4)
    img = img.resize((x2, y2), Image.ANTIALIAS)
    byte_io = io.BytesIO()
    img.save(byte_io, format='PNG', quality=50)
    print ("storing image size: " + str(byte_io.getbuffer().nbytes/1024/1024) + " MB")
    photo.data = Binary(byte_io.getvalue())

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
    obj = photo["data"]
    return send_file(io.BytesIO(obj), mimetype='image/jpeg')
