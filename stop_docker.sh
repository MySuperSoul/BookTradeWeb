#!/usr/bin/env bash
docker-compose down
docker-compose rm
docker image prune -f
docker volume prune -f
docker container prune -f
echo "Docker container all removed, you can rebuild again."