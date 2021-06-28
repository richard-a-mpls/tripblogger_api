
import requests

class AuthorizationExtensions:

    check_token_url = "https://graph.facebook.com/debug_token?input_token={}&access_token={}"
    user_details_url = "https://graph.facebook.com/{}?fields=id,name,email&access_token={}"

    def process_authentication(self, graph_domain, token):
        print ("asdf")


    def check_token(self, token):
        response = requests.get(self.get_fb_token_url(token));
        json_resp = response.json()
        print ("resp is " + str(json_resp))
        print ("App ID: " + json_resp['data']['app_id'])
        self.get_user_details(json_resp['data']['user_id'], token)
        # is_valid, expires_at, user_id, app_id

    def get_user_details(self, user_id, token):
        response = requests.get(self.get_fb_user_url(user_id, token))
        json_resp = response.json()
        print ("name, email " + json_resp["name"] + ":" + json_resp["email"])

    def get_fb_token_url(self, token):
        return self.check_token_url.format(token, token)

    def get_fb_user_url(self, user_id, token):
        return self.user_details_url.format(user_id, token)
