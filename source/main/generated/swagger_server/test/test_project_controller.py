# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.project import Project  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProjectController(BaseTestCase):
    """ProjectController integration test stubs"""

    def test_add_project(self):
        """Test case for add_project

        create a project
        """
        body = Project()
        response = self.client.open(
            '/v1/me/projects',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_session_projects(self):
        """Test case for get_session_projects

        get a project based on authorized session
        """
        response = self.client.open(
            '/v1/me/projects',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
