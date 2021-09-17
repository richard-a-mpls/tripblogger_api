#!/bin/bash

./build.sh

cd ./target
az webapp up --name tripblogger-api