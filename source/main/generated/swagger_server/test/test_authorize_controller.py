# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.authorization_request import AuthorizationRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthorizeController(BaseTestCase):
    """AuthorizeController integration test stubs"""

    def test_authorize(self):
        """Test case for authorize

        authorize a session for token
        """
        body = AuthorizationRequest()
        response = self.client.open(
            '/v1/authorize',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
