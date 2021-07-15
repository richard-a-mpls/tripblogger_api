# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestPhotoController(BaseTestCase):
    """PhotoController integration test stubs"""

    def test_get_photo(self):
        """Test case for get_photo

        get a photo
        """
        response = self.client.open(
            '/v1/photos/{photo_id}'.format(photo_id='photo_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
