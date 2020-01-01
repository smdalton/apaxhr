#!/bin/bash

docker-compose -f docker_compose_files/docker-compose.prod.yml build
docker-compose -f docker_compose_files/docker-compose.prod.yml up