#!/bin/bash

docker-compose -f docker_compose_files/docker-compose.demo.yml build
docker-compose -f docker_compose_files/docker-compose.demo.yml up