#! /bin/bash


docker-compose -f development-docker-compose.yml run api_development ./manage.py startapp api
