#!/bin/bash

git pull
python manage.py makemigrations &&
python manage.py makemigrations auth &&
python manage.py makemigrations ng &&
python manage.py migrate auth &&
python manage.py migrate &&
python manage.py migrate ng &&
python manage.py collectstatic --noinput &&

touch main_site/wsgi.py
