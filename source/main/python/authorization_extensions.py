
import requests
import jwt
import os
import time
from swagger_server.extensions.mongo_interface import MongoInterface

class AuthorizationExtensions:

    check_token_url = "https://graph.facebook.com/debug_token?input_token={}&access_token={}"
    user_details_url = "https://graph.facebook.com/{}?fields=id,name,email&access_token={}"

    def process_authentication(self, graph_domain, token):
        check_token_response = self.check_token(token)
        if not check_token_response:
            print ("check token response returned False")
            return False

        m_interface = MongoInterface()
        user_details_json = self.get_user_details(check_token_response['user_id'], token)
        # TODO need to auto create profile if one isn't already in, and associate to session
        found_profile = m_interface.get_profile_by_identity("fb", user_details_json["id"])
        if found_profile is None:
            # need to create a new profile
            profile_json = {
                "identity_id": user_details_json["id"],
                "identity_issuer": graph_domain,
                "profile_name": user_details_json["name"]
            }
            m_interface.create_profile(profile_json)
            found_profile = m_interface.get_profile_by_identity(graph_domain, user_details_json["id"])



        jwt_contents = {"profile_id": str(found_profile["_id"]), "profile_name": found_profile["profile_name"], "expires": int(time.time())*100000}
        encoded_jwt = jwt.encode(jwt_contents, os.environ["jwt_secret"], algorithm="HS256")
        return encoded_jwt

    def check_token(self, token):
        response = requests.get(self.get_fb_token_url(token));
        json_resp = response.json()
        print ("resp is " + str(json_resp))
        print ("App ID: " + json_resp['data']['app_id'])

        if json_resp['data']["is_valid"] != True:
            print ("token is_valid responded with not True")
            return False

        if os.environ["fb_app_id"] != json_resp['data']['app_id']:
            print ("incorrect app id issued for fb")
            return False

        if int(time.time()) > json_resp['data']['expires_at']:
            print ("token has expired from fb")
            return False

        return json_resp['data']

    def get_user_details(self, user_id, token):
        response = requests.get(self.get_fb_user_url(user_id, token))
        json_resp = response.json()
        print ("name, email " + json_resp["name"] + ":" + json_resp["email"])
        return json_resp

    def get_fb_token_url(self, token):
        return self.check_token_url.format(token, token)

    def get_fb_user_url(self, user_id, token):
        return self.user_details_url.format(user_id, token)
