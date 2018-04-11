# Example Geo-Capable Django RestFramework using Docker

Simple Example Repo to quickstart a DRF API within a Docker Container

Allows for multiple environments to run API, through series of docker-compose files. You should be able to replace the Django Code, making a few updates and get this running

## Main Parts of Repo:

DOCKER related:

* env.sample - A sample env file to setup environmental variables
* bin directory - directory to store your startup and entrypoint scripts.
* Backups directory - directory will store any database backups to restore into the local database Container, also restore script
* Docker-Compose Files -  4 files which compose containers and networking for each environment:
    * development-docker-compose.yml - This is a local dev environment, will spin up a local api container connecting with a local db. It will run the Django Dev Server with the DEBUG variable set to True.
    * staging-docker-compose.yml - This is set to run a production-like environment, creating a api container running with gunicorn server, and green database pooling. It removes the local development from the stack, connecting to a remote database for which the variables/creds are entered into the staging vars in the .env file
    * travis-docker-compose.yml - Deploy version of docker-compose file
    * testing-docker-compose.yml - configures testing version of the API
* DOCKERFILEs:
  * DOCKERFILE.db.development - The DOCKERFILE for local database container
  * DOCKERFILE.api.development - The DOCKERFILE for local api container
  * DOCKERFILE.api.staging - The DOCKERFILE for local api container

API Related:

* gunicorn_config.py - Config file for the gunicorn server

## Run the Sample

There is currently a Sample API included within the repo. To run:

1. `cd` into root of directory and run command `cp env.sample .env`

2. Build the development containers using the command: `./bin/build.sh -l`. If you cannot run you may need to confirm you have executable perms on all the scripts in the `./bin` folder: `$ chmod +x ./bin/*.sh` Feel free to read each one and assign perms individually, cause it is your computer :stuck_out_tongue_winking_eye: and security is a real thing.

3. Once this completes you will now want to start up the project. We will use the start.sh script for this, again using the `-l` flag to run locally:  `./bin/start.sh -l` The first time you run this you will see the database restores. You will also see the api container start up.

4. Open your browser and you will be able to access the Django Rest Framework browserable front end at `http://localhost:8000/api`, the Swagger API schema at `http://localhost:8000/schema`.

5. You can stop the container using ctrl-c to stop the process in the terminal window.


## Quickstart for your own API - Development

Once you understand the sample you can create your own api. Once you do this it will delete the sample, replacing the files with your own.

1. Set a local environment variable for the project title. This will need to be a django/python compliant name.:
`export PROJECT_NAME=dead_songs`

2. `cp env.sample .env` in the root of the repo (this file is already in the .gitignore, so you should not have to worry about it being checked into github)

3. To begin with setup you local variables, ignoring the staging ones at this time:

```
PROJECT_NAME=<What you want to name the project>
# keep as true to run the django dev server
DEBUG=True

# the database superuser name - this is the default
DEVELOPMENT_POSTGRES_USER=postgres

# the database name the API will connect to - "dbname" in most PostgreSQL command-line tools
DEVELOPMENT_POSTGRES_NAME=<your_database_name>

# *service* name (*not* image name) of the database in the Docker network
DEVELOPMENT_POSTGRES_HOST=db_development

# port the database is listening on in the Docker network
DEVELOPMENT_POSTGRES_PORT=5432

# password for the PostgreSQL database superuser in the database container
DEVELOPMENT_POSTGRES_PASSWORD=sit-down-c0mic

# Django secret key in the API container
DEVELOPMENT_DJANGO_SECRET_KEY=r0ck.ar0und.the.c10ck
```

4. Copy you database backup into the backup folder. Database container is a Postgis-enabled 9.6 container. Backup can be a .backup, .sql, or .sql.gz format.

5. Run the create-project script: `./bin/create-project.sh` (This will delete all files related to the sample app and replace with a new django restframework app with your project name. It will also replace the default settings.py file with the sample.py, which has been pre configured a bit for our stack.)

6. Run the create-app script: `./bin/create-app.sh` (This will create the restframework api in a folder called api)
