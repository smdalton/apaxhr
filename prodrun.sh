#!/bin/bash

docker-compose -f docker-compose.prod.yml build
exec docker-compose -f docker-compose.prod.yml up