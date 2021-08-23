import jwt
from swagger_server.utilities.jwksutils import rsa_pem_from_jwk  # <-- this module contains the piece of code described previously
import time
# obtain jwks as you wish: configuration file, HTTP GET request to the endpoint returning them;

jwks_url = "https://rcaazdemo.b2clogin.com/rcaazdemo.onmicrosoft.com/b2c_1_bloggersignin/discovery/v2.0/keys"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsifQ.eyJleHAiOjE2Mjk1NzQwODMsIm5iZiI6MTYyOTU3MDQ4MywidmVyIjoiMS4wIiwiaXNzIjoiaHR0cHM6Ly9yY2FhemRlbW8uYjJjbG9naW4uY29tLzYyYzgyZDliLTcyZmQtNDgwNS1iZmZmLTlhODQ4ZGUxNjc5Ni92Mi4wLyIsInN1YiI6ImE2OGU4NDU4LWNlZDEtNGI3NC05MjBjLWJkZmY2ZWEzYzcwMCIsImF1ZCI6IjkzNzVkYmEyLTRlNWYtNDM3Ny04NjNlLWIyMzFjNjA4ZWFkYSIsIm5vbmNlIjoiY2RmYjY4ZTEtMzJkMS00N2FiLTkxNGYtYTg5OGYzNzRlMDA0IiwiaWF0IjoxNjI5NTcwNDgzLCJhdXRoX3RpbWUiOjE2Mjk1NzA0ODMsIm9pZCI6ImE2OGU4NDU4LWNlZDEtNGI3NC05MjBjLWJkZmY2ZWEzYzcwMCIsIm5hbWUiOiJSaWNoIFVzZXIiLCJlbWFpbHMiOlsicmNhQHJpY2guY28iXSwidGZwIjoiQjJDXzFfQkxvZ2dlclNpZ25pbiJ9.UugiHqjOAQh3_1GsbQC8I3eYAGTXxUyiA_OL_c1XTwzMPXek8IAyHKDRL8O8vSeVhSDsYRfWmrUDfgfbFXKP2wlHPM_vHFSp7MYC8h6H2RaRKTNhK112-oz0z9i20vvKDqpIDXicBSginox3UIVE_OaKsbDxi8RqJkR89r2l8r249SOYJvofEINW6zSSxmJVts-S4gzWRatxCS-8V_SXS6iM-9WeAsaeShiox3ZM5Wz7Ku2txe-w24-ZXlXoaOMJSWJTlKxcf43iZmjNwYd_MSc4lyvK3FvaTFiRb-zJ6ocUdAV5FCr0rdTYNNuXlafUVBVStayTWRpbhB9i--8low"
jwks = {
    "keys": [
        {"kid":"X5eXk4xyojNFum1kl2Ytv8dlNP4-c57dO6QGTVBwaNk","nbf":1493763266,"use":"sig","kty":"RSA","e":"AQAB","n":"tVKUtcx_n9rt5afY_2WFNvU6PlFMggCatsZ3l4RjKxH0jgdLq6CScb0P3ZGXYbPzXvmmLiWZizpb-h0qup5jznOvOr-Dhw9908584BSgC83YacjWNqEK3urxhyE2jWjwRm2N95WGgb5mzE5XmZIvkvyXnn7X8dvgFPF5QwIngGsDG8LyHuJWlaDhr_EPLMW4wHvH0zZCuRMARIJmmqiMy3VD4ftq4nS5s8vJL0pVSrkuNojtokp84AtkADCDU_BUhrc2sIgfnvZ03koCQRoZmWiHu86SuJZYkDFstVTVSR0hiXudFlfQ2rOhPlpObmku68lXw-7V-P7jwrQRFfQVXw"}
    ]
}

# configuration, these can be seen in valid JWTs from Azure B2C:
# TODO set these as env vars
valid_audiences = ['3a5d7d6a-6380-48dc-b027-7fb3a6270409']  # id of the application prepared previously
issuer = 'https://rcaazdemo.b2clogin.com/62c82d9b-72fd-4805-bfff-9a848de16796/v2.0/'  # iss


class InvalidAuthorizationToken(Exception):
    def __init__(self, details):
        super().__init__('Invalid authorization token: ' + details)


def get_kid(token):
    headers = jwt.get_unverified_header(token)
    if not headers:
        raise InvalidAuthorizationToken('missing headers')
    try:
        return headers['kid']
    except KeyError:
        raise InvalidAuthorizationToken('missing kid')


def get_jwk(kid):
    for jwk in jwks.get('keys'):
        if jwk.get('kid') == kid:
            return jwk
    raise InvalidAuthorizationToken('kid not recognized')


def get_public_key(token):
    return rsa_pem_from_jwk(get_jwk(get_kid(token)))


def validate_jwt(jwt_to_validate):
    public_key = get_public_key(jwt_to_validate)
    #TODO need to work around the need for this sleep.
    #time.sleep(1) # we seem to be 1 ms ahead of the iat and nbf timestamps
    decoded = jwt.decode(jwt_to_validate,
                         public_key,
                         verify=True,
                         algorithms=['RS256'],
                         audience=valid_audiences,
                         issuer=issuer,
                         options={"verify_nbf": False})

    # do what you wish with decoded token:
    # if we get here, the JWT is validated
    current_time = time.time()-5

    if current_time > decoded["nbf"]:
        raise "Token NBF is too early"

    print(decoded)
    return decoded


def extract_token(token):
    import traceback

    print ("validate " + token);
    if not token:
        print('Please pass a valid JWT')

    try:
        decoded = validate_jwt(token)
    except Exception as ex:
        traceback.print_exc()
        print('The JWT is not valid!')
        return None;
    else:
        print('The JWT is valid!')
    return decoded


# if __name__ == '__main__':
#     main()
