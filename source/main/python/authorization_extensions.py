
import requests
import jwt
import os
import time
from swagger_server.extensions.mongo_interface import MongoInterface
from swagger_server.utilities import b2c_token_validator

class AuthorizationExtensions:

    def process_authentication(self, graph_domain, token):
        idp = "b2c"
        print (token)
        decoded_token = b2c_token_validator.extract_token(str(token))
        print(decoded_token)

        if 'idp' in decoded_token:
            idp = decoded_token['idp']

        m_interface = MongoInterface()
        found_profile = m_interface.get_profile_by_identity(idp, decoded_token["sub"])
        if found_profile is None:
            # need to create a new profile
            profile_json = {
                "identity_id": decoded_token["sub"],
                "identity_issuer": idp,
                "profile_name": decoded_token["name"]
            }

            m_interface.create_profile(profile_json)
            found_profile = m_interface.get_profile_by_identity(idp, decoded_token["sub"])

        jwt_contents = {"profile_id": str(found_profile["_id"]), "profile_name": found_profile["profile_name"], "expires": int(time.time())*100000}
        encoded_jwt = jwt.encode(jwt_contents, os.environ["jwt_secret"], algorithm="HS256")
        return encoded_jwt