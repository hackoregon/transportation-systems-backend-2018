#!/bin/bash
export PATH=$PATH:~/.local/bin


set -e

>&2 echo "Postgres is up"


# ./manage.py test --keepdb --noinput
pytest
