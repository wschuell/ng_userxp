#!/bin/bash

#apt-get install --yes --force-yes postgresql postgresql-contrib libpq-dev


psql -c "createdb ng_userxp;" -U postgres
psql -c "CREATE USER ng_userxp_user WITH PASSWORD 'pass';" -U postgres
psql -c "createdb naminggames;"  -U postgres
psql -c "CREATE USER naminggames WITH PASSWORD 'naminggames';" -U postgres

DJANGO_MODULE_SETTINGS="main_site.production_settings"
export DJANGO_MODULE_SETTINGS
python manage.py makemigrations ng
python manage.py migrate
python manage.py collectstatic
