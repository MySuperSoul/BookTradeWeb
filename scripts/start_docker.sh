#!/usr/bin/env bash
docker-compose build
docker-compose up -d

echo "You may need 20-30s for service container start and initial. Then you can visit website by IP:8000. e.t. localhost:8000"