import connexion
from swagger_server.extensions.mongo_interface import MongoInterface
from swagger_server.utilities.file_transformation import FileTransformation


def add_project_photo(project_id, file_name=None):  # noqa: E501
    """upload a photo to your project.

    upload a photo to your project # noqa: E501

    :param project_id: ID of project to delete
    :type project_id: str
    :param file_name: 
    :type file_name: strstr

    :rtype: None
    """

    user_profile = connexion.request.authorization["profile_id"]
    m_interface = MongoInterface()
    project = m_interface.get_project(project_id)

    if project["profile_id"] != user_profile:
        print ("profile ID does not match")
        return {"status": 401, "reason": "Not Authorized"}

    uploaded_file = connexion.request.files['file']


    file_transform = FileTransformation()
    photo = file_transform.transform(uploaded_file)

    header = uploaded_file.stream.read(512)
    uploaded_file.stream.seek(0)

    m_interface = MongoInterface()
    inserted_id = m_interface.create_photo(photo.to_dict())
    #TODO, define proper return object and refactor.
    #return {'id': inserted_id}
    m_interface.append_project_photo(project_id, inserted_id)

    return {'id': inserted_id}
