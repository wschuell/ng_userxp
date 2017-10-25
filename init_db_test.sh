#!/bin/bash

#apt-get install --yes --force-yes postgresql postgresql-contrib libpq-dev

su - postgres << 'EOF'
service postgresql start
createdb ng_userxp
psql -c "CREATE USER ng_userxp_user WITH PASSWORD 'pass';"
createdb naminggames
psql -c "CREATE USER naminggames WITH PASSWORD 'naminggames';"
EOF

DJANGO_MODULE_SETTINGS="main_site.production_settings"
export DJANGO_MODULE_SETTINGS
python manage.py makemigrations ng
python manage.py migrate
python manage.py collectstatic
