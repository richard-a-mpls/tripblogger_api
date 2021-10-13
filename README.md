# tripblogger_api

python flask implementation for handling tripblogger a.k.a. slackr. 

This api implementation handles profile based activities as well as areas concerning images.

Plan going forward is to move the profile actions to a NodeJS microservice so this can focus just on images.

Additionally this will be refactored to use a common JWT verification API hosted by a springboot microservice.

The following runtime attributes are expected:

MONGO_URI - the mongo url to the mongo instance used
MONGO_DATABASE - the database name to use
TOKEN_ISSUER - the B2C Issuer for JWT verification
TOKEN_AUDIENCE - the expected Audience for JWT verification
JWKS_URL - the JWKS URL endpoint for JWT verification
