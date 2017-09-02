#!/bin/bash
service postgresql start

su - postgres << 'EOF'
createdb ng_userxp
psql -c "CREATE USER ng_userxp_user WITH PASSWORD 'pass';"
createdb naminggames
psql -c "CREATE USER naminggames WITH PASSWORD 'naminggames';"
EOF

DJANGO_MODULE_SETTINGS="main_site.production_settings"
export DJANGO_MODULE_SETTINGS
python manage.py collectstatic
