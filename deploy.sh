#!/bin/sh

#export AWS_ACCESS_KEY_ID=
#export AWS_SECRET_ACCESS_KEY=

pipenv lock -r > app/functions/requirements.txt

cd `dirname $0`/app

sam build

sam deploy \
  --stack-name SAM-apispec \
  --config-env dev \
  --config-file samconfig.toml
