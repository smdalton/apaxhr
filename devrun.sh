#!/bin/bash

docker kill dev_app
docker-compose -f docker_compose_files/docker_compose.dev.yml down -v
docker-compose -f docker_compose_files/docker-compose.dev.yml build
docker-compose -f docker_compose_files/docker-compose.dev.yml up