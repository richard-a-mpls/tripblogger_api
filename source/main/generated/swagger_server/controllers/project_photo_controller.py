import connexion
import six
from swagger_server.extensions.mongo_interface import MongoInterface
from swagger_server import util
from bson.binary import Binary
import imghdr
from swagger_server.models.photo import Photo
from PIL import Image
import math
import io


def add_project_photo(project_id, file_name=None):  # noqa: E501
    """upload a photo to your project.

    upload a photo to your project # noqa: E501

    :param project_id: ID of project to delete
    :type project_id: str
    :param file_name: 
    :type file_name: strstr

    :rtype: None
    """

    user_profile = connexion.request.authorization["user_profile"]
    m_interface = MongoInterface()
    project = m_interface.get_project(project_id)

    if project["profile_id"] != user_profile:
        print ("profile ID does not match")
        return {"status": 401, "reason": "Not Authorized"}

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
    #return {'id': inserted_id}
    m_interface.append_project_photo(project_id, inserted_id)

    return {'id': inserted_id}
