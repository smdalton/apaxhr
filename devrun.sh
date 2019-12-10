#!/bin/bash

# exec docker-compose -f docker-compose.dev.yml down
docker-compose -f docker-compose.dev.yml build
exec docker-compose -f docker-compose.dev.yml up