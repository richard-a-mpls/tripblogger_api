# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.photo import Photo  # noqa: F401,E501
from swagger_server import util


class ProjectDay(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, summary: str=None, description: str=None, location: str=None, _date: str=None, photos: List[Photo]=None):  # noqa: E501
        """ProjectDay - a model defined in Swagger

        :param id: The id of this ProjectDay.  # noqa: E501
        :type id: str
        :param summary: The summary of this ProjectDay.  # noqa: E501
        :type summary: str
        :param description: The description of this ProjectDay.  # noqa: E501
        :type description: str
        :param location: The location of this ProjectDay.  # noqa: E501
        :type location: str
        :param _date: The _date of this ProjectDay.  # noqa: E501
        :type _date: str
        :param photos: The photos of this ProjectDay.  # noqa: E501
        :type photos: List[Photo]
        """
        self.swagger_types = {
            'id': str,
            'summary': str,
            'description': str,
            'location': str,
            '_date': str,
            'photos': List[Photo]
        }

        self.attribute_map = {
            'id': '_id',
            'summary': 'summary',
            'description': 'description',
            'location': 'location',
            '_date': 'date',
            'photos': 'photos'
        }
        self._id = id
        self._summary = summary
        self._description = description
        self._location = location
        self.__date = _date
        self._photos = photos

    @classmethod
    def from_dict(cls, dikt) -> 'ProjectDay':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProjectDay of this ProjectDay.  # noqa: E501
        :rtype: ProjectDay
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this ProjectDay.


        :return: The id of this ProjectDay.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ProjectDay.


        :param id: The id of this ProjectDay.
        :type id: str
        """

        self._id = id

    @property
    def summary(self) -> str:
        """Gets the summary of this ProjectDay.


        :return: The summary of this ProjectDay.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary: str):
        """Sets the summary of this ProjectDay.


        :param summary: The summary of this ProjectDay.
        :type summary: str
        """

        self._summary = summary

    @property
    def description(self) -> str:
        """Gets the description of this ProjectDay.


        :return: The description of this ProjectDay.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ProjectDay.


        :param description: The description of this ProjectDay.
        :type description: str
        """

        self._description = description

    @property
    def location(self) -> str:
        """Gets the location of this ProjectDay.


        :return: The location of this ProjectDay.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this ProjectDay.


        :param location: The location of this ProjectDay.
        :type location: str
        """

        self._location = location

    @property
    def _date(self) -> str:
        """Gets the _date of this ProjectDay.


        :return: The _date of this ProjectDay.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date: str):
        """Sets the _date of this ProjectDay.


        :param _date: The _date of this ProjectDay.
        :type _date: str
        """

        self.__date = _date

    @property
    def photos(self) -> List[Photo]:
        """Gets the photos of this ProjectDay.


        :return: The photos of this ProjectDay.
        :rtype: List[Photo]
        """
        return self._photos

    @photos.setter
    def photos(self, photos: List[Photo]):
        """Sets the photos of this ProjectDay.


        :param photos: The photos of this ProjectDay.
        :type photos: List[Photo]
        """

        self._photos = photos
