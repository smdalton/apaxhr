#!/bin/bash

docker-compose -f docker-compose.dev.yml build
exec docker-compose -f docker-compose.dev.yml up