#!/bin/bash

cd ng
python gen_json_str.py || (cd .. && exit 1)
cd ..

git pull
python manage.py makemigrations &&
python manage.py makemigrations auth &&
python manage.py makemigrations ng &&
python manage.py migrate auth &&
python manage.py migrate &&
python manage.py migrate ng &&
python manage.py collectstatic --noinput &&

touch main_site/wsgi.py
