import connexion
import six
from swagger_server.extensions.mongo_interface import MongoInterface
from swagger_server.models.project import Project, ProjectDay  # noqa: E501
from swagger_server.models.photo import Photo
from swagger_server import util
import time
import uuid
from bson.binary import Binary
import imghdr
import io
from PIL import Image
import math


def add_project(body):  # noqa: E501
    """create a project

    create a project # noqa: E501

    :param id: 
    :type id: str
    :param profile_id: 
    :type profile_id: str
    :param summary: 
    :type summary: str
    :param description: 
    :type description: str
    :param location: 
    :type location: str
    :param published: 
    :type published: bool
    :param showcase_photo_id: 
    :type showcase_photo_id: str
    :param share_with: 
    :type share_with: str
    :param project_days: 
    :type project_days: list | bytes

    :rtype: None
    """

    body = Project.from_dict(body)
    body.profile_id=connexion.request.authorization["user_profile"]
    if body.published is None:
        body.published = False
    if body.share_with is None:
        body.share_with = "private"

    # Setup a placeholder project day
    current_date_str = time.strftime('%Y-%m-%d')

    if body.project_days is None:
        project_day = ProjectDay()
        project_day.summary = body.summary
        project_day.description = body.description
        project_day.location = body.location
        project_day.datestmp = current_date_str
        project_day.id = str(uuid.uuid4())
        project_days = [project_day]
    else:
        for pd in body.project_days:
            pd.id = str(uuid.uuid4())
            if pd.summary is None:
                pd.summary = body.summary
            if pd.description is None:
                pd.description = body.description
            if pd.location is None:
                pd.location = body.location
            if pd.datestmp is None:
                pd._date = current_date_str


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
    created_id = m_interface.create_photo(photo.to_dict())
    body.showcase_photo_id = created_id

    response = m_interface.create_project(body.to_dict())
    return_project = Project.from_dict(response)

    # TODO - update swagger spec to add return object.
    return return_project

def delete_project(project_id):  # noqa: E501
    """delete a project by id

    delete that project # noqa: E501

    :param project_id: ID of project to delete
    :type project_id: str

    :rtype: None
    """
    profile_id = connexion.request.authorization["user_profile"]
    m_interface = MongoInterface()
    project_to_delete = m_interface.get_project(project_id)

    if project_to_delete["profile_id"] != profile_id:
        print ("profile ID does not match")
        return {"status": 401, "reason": "Not Authorized"}
    if project_to_delete["showcase_photo_id"] is not None:
        m_interface.delete_photo(project_to_delete["showcase_photo_id"])
    m_interface.delete_project(project_id)
    return {"status": 200, "description": "Deleted " + project_id}


def get_project(project_id):  # noqa: E501
    """get a project by id

    get that project # noqa: E501

    :param project_id: ID of project to return
    :type project_id: str

    :rtype: Project
    """
    m_interface = MongoInterface()
    prj = m_interface.get_project(project_id)
    return Project.from_dict(prj)


def get_session_projects():  # noqa: E501
    """get a project based on authorized session

     # noqa: E501


    :rtype: List[Project]
    """
    profile_id = connexion.request.authorization["user_profile"]
    m_interface = MongoInterface()
    res_count, results = m_interface.get_projects(profile_id)
    resp_list = list()
    for res in results:
        resp_list.append(Project.from_dict(res))
    return resp_list

def patch_project(body, project_id):  # noqa: E501
    """update attributes of a project

     # noqa: E501"""
    profile_id = connexion.request.authorization["user_profile"]
    m_interface = MongoInterface()
    project_to_patch = m_interface.get_project(project_id)

    if project_to_patch["profile_id"] != profile_id:
        print ("profile ID does not match")
        return {"status": 401, "reason": "Not Authorized"}

    m_interface.patch_project(project_id, body)
    return Project.from_dict(m_interface.get_project(project_id))





