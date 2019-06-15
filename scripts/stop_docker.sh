#!/usr/bin/env bash
docker-compose down
docker-compose rm
docker image prune -f
docker container prune -f
docker volume prune -f