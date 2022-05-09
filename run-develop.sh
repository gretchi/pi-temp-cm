#!/bin/bash

this_dir=$(cd $(dirname $0) && pwd)

echo "${this_dir}"

export FLASK_DEBUG=1
export DEVELOP=1

cd "${this_dir}/driver"
docker-compose -p pt-driver -f "${this_dir}/driver/docker-compose.yml" up -d

cd "${this_dir}/controller"
docker-compose -p pt-controller -f "${this_dir}/controller/docker-compose.yml" up -d
