#!/usr/bin/env python3

import connexion
from flask_cors import CORS
from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'API Title'}, pythonic_params=True)
    CORS(app.app)
    #cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})
    app.run(port=8080)


if __name__ == '__main__':
    main()
