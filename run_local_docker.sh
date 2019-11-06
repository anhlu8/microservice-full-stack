#!/usr/bin/env bash

cd server
docker build --tag=flask-server .
docker image ls
docker run -p 8000:5000 -v /Users/anh/Desktop/containerized-app/server:/flask flask-server