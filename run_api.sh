#!/bin/bash

./build.sh

cd target
source .venv/bin/activate
python3 -m swagger_server