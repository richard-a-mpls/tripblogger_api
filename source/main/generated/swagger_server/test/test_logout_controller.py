# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestLogoutController(BaseTestCase):
    """LogoutController integration test stubs"""

    def test_logout(self):
        """Test case for logout

        de-authorize a session for token
        """
        response = self.client.open(
            '/v1/logout',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
