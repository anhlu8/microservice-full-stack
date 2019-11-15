#!/usr/bin/env bash

cd client/
npm run build
aws s3 ls
aws s3 cp build/ s3://static-react-app/ --recursive