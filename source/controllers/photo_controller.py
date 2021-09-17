import connexion
from swagger_server.mongo.mongo_interface import MongoInterface
from flask import send_file, request
import io
from swagger_server.utilities.file_transformation import FileTransformation

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

    file_transform = FileTransformation()
    photo = file_transform.transform(uploaded_file)

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
