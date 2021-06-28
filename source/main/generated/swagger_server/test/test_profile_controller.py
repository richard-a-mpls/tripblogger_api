# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.profile import Profile  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProfileController(BaseTestCase):
    """ProfileController integration test stubs"""

    def test_add_profile(self):
        """Test case for add_profile

        create a profile
        """
        body = Profile()
        response = self.client.open(
            '/v1/profile',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_profile(self):
        """Test case for get_profile

        get a profile by id
        """
        response = self.client.open(
            '/v1/profile/{profileId}'.format(profile_id='profile_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
