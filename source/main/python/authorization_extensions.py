
import requests
import os
import time
import uuid
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
        # first see if a session already exists for this token
        api_session = m_interface.find_token_session(token, graph_domain)
        if api_session is not None:
            print ("Api session found, let's return it" + str(api_session))
            return str(api_session["api_token"])

        print ("Api session not found, let's create one based on user details")
        user_details_json = self.get_user_details(check_token_response['user_id'], token)

        # TODO need to auto create profile if one isn't already in, and associate to session
        session_json = {"identity_token": token,
                        "identity_issuer": graph_domain,
                        "api_token": uuid.uuid4(),
                        "api_token_expiration": int(time.time())*100000,
                        "profile": {
                            "user_id": user_details_json["id"],
                            "name": user_details_json["name"],
                            "email": user_details_json["email"]
                        }}

        inserted_id = m_interface.create_session(session_json)
        print ("created new api session with id: " + str(inserted_id) + " api_token of " + str(session_json["api_token"]))
        return str(session_json["api_token"])

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
