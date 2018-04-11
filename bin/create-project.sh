#! /bin/bash

rm  manage.py
rm -rf dead_songs
rm -rf api

docker-compose -f development-docker-compose.yml run api_development django-admin.py startproject $PROJECT_NAME .

rm $PROJECT_NAME/settings.py
cp ./bin/example-settings.py $PROJECT_NAME/settings.py

sed -i '' 's/\<EXAMPLE_PROJECT_NAME\>/'$PROJECT_NAME'/g' $PROJECT_NAME/settings.py
