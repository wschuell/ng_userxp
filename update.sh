#!/bin/bash

git pull
python manage.py makemigrations ng
python manage.py migrate
python manage.py collectstatic --noinput
touch main_site/wsgi.py