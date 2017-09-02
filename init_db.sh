#!/bin/bash
service postgresql start

su - postgres
createdb ng_userxp
psql -c "CREATE USER ng_userxp_user WITH PASSWORD 'pass';"

createdb naminggames
psql -c "CREATE USER naminggames WITH PASSWORD 'naminggames';"
exit

DJANGO_MODULE_SETTINGS="main_site.production_settings"
export DJANGO_MODULE_SETTINGS
RUN python manage.py makemigrations ng && python manage.py migrate
RUN python manage.py collectstatic
