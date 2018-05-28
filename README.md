# Transportation Systems 2018 Backend Project

This project contains the Django Rest Framework (DRF) project and API applications for the Hack Oregon 2018 Transportation Systems Team. It is an iteration on the earlier stand-alone repos.

Allows for multiple environments to run API, through series of docker-compose files.

## Main Parts of Repo

DOCKER related:

* `env.sample` - A sample env file to setup environmental variables
* bin directory - directory containing the startup and entrypoint scripts:
  * `build.sh` - This script runs a `docker-compose build` command, accepts 2 flags:
    * `-d` - Builds containers based on the `development-docker-compose.yml` file
    * `-p` - Builds containers based on the `production-docker-compose.yml` file
  * `start.sh` - This script runs a `docker-compose up` command, starting the containers and apps, accepts 2 flags:
    * `-d` - Starts containers based on the `development-docker-compose.yml` file
    * `-p` - Starts containers based on the `production-docker-compose.yml` file
  * `test.sh` - This script spins up and runs tests in test containers. and removes test container once the script is complete
  * Entrypoint scripts - These are run within the api container when `docker-compose up` is run:
    * `development-docker-entrypoint.sh` - Startup tasks for development container
    * `production-docker-entrypoint.sh` - Startup tasks for production container
    * `test-entrypoint.sh` -  Startup tasks for testing container
* Docker-Compose Files -  2 files which compose containers and networking for each environment:
  * `development-docker-compose.yml` - This is a local dev environment, will spin up a local api container connecting with a local db. It will run the Django Dev Server with the DEBUG variable set to True.
  * `production-docker-compose.yml` - This is set to run a production-like environment, creating a api container running with gunicorn server, and green database pooling. It removes the local development database from the stack, connecting to a remote database for which the variables/creds are entered into the production vars in the `.env` file
* DOCKERFILEs:
  * `DOCKERFILE.db.development` - The DOCKERFILE for local database container
  * `DOCKERFILE.api.development` - The DOCKERFILE for local api container
  * `DOCKERFILE.api.production` - The DOCKERFILE for a production build of api

API Related:

* `gunicorn_config.py` - Config file for the gunicorn server
* `transportation_systems_2018` folder - This is the main Django Project folder contains:
  * `settings.py` - This file contains the settings for the Project
  * `urls.py` - Base urls file, registers swagger as well as the individual APIs
  * `router.py` - Custom database router, which allows for the multiple database/schemas to be used
* `<DATASET>_api` folders - each of these folders represent the specific "apps" or individual apis being hosted through this project

## Run the API - Development

1. `cp env.sample .env` in the root of the repo (this file is already in the `.gitignore`, so you should not have to worry about it getting accidentally checked into a GitHub repo)

2. Edit your `.env` file and change the variables to appropriate values for your project's database backup. Ensure that the values `PROJECT_NAME`, `POSTGRES_NAME`, and `DATABASE_OWNER` are set correctly. You should not need to change any of the other values. _If you unsure of what values to use for these settings or do not have a database backup file, please contact your Team's Data Manager before proceeding further._


```
PROJECT_NAME=dead_songs

# the database superuser name - this is the default
POSTGRES_USER=postgres

# the database name the API will connect to - "dbname" in most PostgreSQL command-line tools
POSTGRES_NAME=dead_songs

# the database owner - automatic restore needs this (most likely only used in dev)
DATABASE_OWNER=sampleuser

# *service* name (*not* image name) of the database in the Docker network
POSTGRES_HOST=db_development

# port the database is listening on in the Docker network
POSTGRES_PORT=5432

# password for the PostgreSQL database superuser in the database container
POSTGRES_PASSWORD=sit-down-c0mic

# the password for the teams
TEAM_PASSWORD=d0wn!0ff!a!duck

# Django secret key in the API container
DJANGO_SECRET_KEY=r0ck.ar0und.the.c10ck
```

3. Build the development containers using the command: `./bin/build.sh -d`. If this script won't run, you may need to confirm you have executable perms on all the scripts in the `./bin` folder: `$ chmod +x ./bin/*.sh` Feel free to read each one and assign perms individually, 'cause it is your computer :stuck_out_tongue_winking_eye: and security is a real thing.

4. Once this completes you will now want to start up the project. We will use the `start.sh` script for this, again using the `-d` flag to run locally:  `./bin/start.sh -d` The first time you run this you will see the database restores. You will also see the api container start up.

5. Open your browser and you will be able to access the Django REST framework browserable front end. The IP address you use will depend on your Docker hosting:

    * Windows 10 Pro + Docker for Windows, MacOS or Linux: API root `http://localhost:8000/transportation-systems/<app>`, Swagger API schema `http://localhost:8000/swagger`
    * Docker Toolbox running on Windows or Mac: API root `http://MACHINE-IP:8000/transportation-systems/<app>`, Swagger API schema `http://MACHINE-IP:8000/swagger`

        where `MACHINE-IP` is the IP address `docker-machine ip` returns.

5. You can stop the container using Ctrl-C to stop the process in the terminal window.

## API Modules

This API serves data covering multiple facets of transporation within the Portland Metro Area. The following is a brief description of each dataset. Consult our Swagger/API Documentation for specific endpoints and example responses.

### Biketown Trips in Portland

### ODOT Crash Data for Portland Metro Region

### SAFE Transportation Safety Hotline Response Tickets

### Trimet Passenger Census

### Trimet Moving Data Stop Events

## Run the Tests

<needs redo>

## About the Multi-tenent application architecture



## Contributors and History

This repo represents the work of many members of the Hack Oregon project team. The roots of this work began with the [2017 backend-service-pattern](https://github.com/hackoregon/backend-service-pattern), the work of the DevOps and platform teams, and the APIs deployed for the 2017 seasons.

This current implementation builds on the [transportation-system-backend](https://github.com/hackoregon/transportation-system-backend) and [passenger_census_api](https://github.com/hackoregon/passenger_census_api). The database structure is an implementation of the PostGIS container of the **data-science-pet-containers** repo.

### Major Contributors

M. Edward (Ed) Borasky ([znmeb](https://github.com/znmeb)),
Brian Grant ([bhgrant8](https://github.com/bhgrant8), [BrianHGrant](https://github.com/BrianHGrant)),
Adi ([kiniadit](https://github.com/kiniadit)),
Mike Lonergan ([mikethecanuck](https://github.com/mikethecanuck)),
Alec Peters ([adpeters](https://github.com/adpeters)),
Nathan Miller ([nam20485](https://github.com/nam20485)).
