#!/bin/bash

# cleanup previous build
rm -rf ./target

# generate latest definitions
./generate_swagger.sh

# copy base swagger server
mkdir ./target
cp -R ./generated/* ./target/

# copy custom code into server
cp ./source/controllers/* ./target/swagger_server/controllers/
cp -R ./source/mongo ./target/swagger_server/
cp -R ./source/utilities ./target/swagger_server/
cp ./source/__main__.py ./target/swagger_server/
cp ./requirements.txt ./target/

# build the venv
cd target
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

