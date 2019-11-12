#!/usr/bin/env bash

aws ecr create-repository --repository-name flask-postgresdb-docker
cd server
docker build -t flask-postgresdb-docker .
docker tag flask-postgresdb-docker 278749303080.dkr.ecr.us-east-1.amazonaws.com/flask-postgresdb-docker:latest
docker push 278749303080.dkr.ecr.us-east-1.amazonaws.com/flask-postgresdb-docker:latest