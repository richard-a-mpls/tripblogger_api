import unittest

from source.main.python.authorization_extensions import AuthorizationExtensions

class MyTestCase(unittest.TestCase):

    def test_get_facebook_token_url(self):
        ae = AuthorizationExtensions()
        self.assertEqual("https://graph.facebook.com/debug_token?input_token=1&access_token=1", ae.get_fb_token_url("1"))

    def test_get_facebook_token_url(self):
        ae = AuthorizationExtensions()
        self.assertEqual("https://graph.facebook.com/1234?fields=id,name,email&access_token=4321", ae.get_fb_user_url("1234", "4321"))

if __name__ == '__main__':
    unittest.main()
