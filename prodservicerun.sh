#!/bin/bash

docker kill dev_app
docker-compose -f docker_compose_files/docker_compose.services.yml down -v
docker-compose -f docker_compose_files/docker-compose.services.yml build
docker-compose -f docker_compose_files/docker-compose.services.yml up