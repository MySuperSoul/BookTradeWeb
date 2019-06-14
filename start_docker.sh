#!/usr/bin/env bash
docker-compose build
docker-compose up -d
docker-compose run web python manage.py migrate
echo "Visit the website using IP:8000(e.g. localhost:8000)"