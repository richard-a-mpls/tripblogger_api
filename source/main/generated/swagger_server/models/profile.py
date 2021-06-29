# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Profile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, profile_id: str=None, profile_name: str=None, identity_issuer: str=None, identity_id: str=None, connections: List=None):  # noqa: E501
        """Profile - a model defined in Swagger

        :param profile_id: The profile_id of this Profile.  # noqa: E501
        :type profile_id: str
        :param profile_name: The profile_name of this Profile.  # noqa: E501
        :type profile_name: str
        :param identity_issuer: The identity_issuer of this Profile.  # noqa: E501
        :type identity_issuer: str
        :param identity_id: The identity_id of this Profile.  # noqa: E501
        :type identity_id: str
        :param connections: The connections of this Profile.  # noqa: E501
        :type connections: List
        """
        self.swagger_types = {
            'profile_id': str,
            'profile_name': str,
            'identity_issuer': str,
            'identity_id': str,
            'connections': List
        }

        self.attribute_map = {
            'profile_id': 'profile_id',
            'profile_name': 'profile_name',
            'identity_issuer': 'identity_issuer',
            'identity_id': 'identity_id',
            'connections': 'connections'
        }
        self._profile_id = profile_id
        self._profile_name = profile_name
        self._identity_issuer = identity_issuer
        self._identity_id = identity_id
        self._connections = connections

    @classmethod
    def from_dict(cls, dikt) -> 'Profile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Profile of this Profile.  # noqa: E501
        :rtype: Profile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def profile_id(self) -> str:
        """Gets the profile_id of this Profile.


        :return: The profile_id of this Profile.
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id: str):
        """Sets the profile_id of this Profile.


        :param profile_id: The profile_id of this Profile.
        :type profile_id: str
        """

        self._profile_id = profile_id

    @property
    def profile_name(self) -> str:
        """Gets the profile_name of this Profile.


        :return: The profile_name of this Profile.
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name: str):
        """Sets the profile_name of this Profile.


        :param profile_name: The profile_name of this Profile.
        :type profile_name: str
        """
        if profile_name is None:
            raise ValueError("Invalid value for `profile_name`, must not be `None`")  # noqa: E501

        self._profile_name = profile_name

    @property
    def identity_issuer(self) -> str:
        """Gets the identity_issuer of this Profile.


        :return: The identity_issuer of this Profile.
        :rtype: str
        """
        return self._identity_issuer

    @identity_issuer.setter
    def identity_issuer(self, identity_issuer: str):
        """Sets the identity_issuer of this Profile.


        :param identity_issuer: The identity_issuer of this Profile.
        :type identity_issuer: str
        """

        self._identity_issuer = identity_issuer

    @property
    def identity_id(self) -> str:
        """Gets the identity_id of this Profile.


        :return: The identity_id of this Profile.
        :rtype: str
        """
        return self._identity_id

    @identity_id.setter
    def identity_id(self, identity_id: str):
        """Sets the identity_id of this Profile.


        :param identity_id: The identity_id of this Profile.
        :type identity_id: str
        """

        self._identity_id = identity_id

    @property
    def connections(self) -> List:
        """Gets the connections of this Profile.


        :return: The connections of this Profile.
        :rtype: List
        """
        return self._connections

    @connections.setter
    def connections(self, connections: List):
        """Sets the connections of this Profile.


        :param connections: The connections of this Profile.
        :type connections: List
        """

        self._connections = connections
