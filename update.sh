#!/bin/bash

git pull
python manage.py makemigrations ng
python manage.py migrate
python manage.py collectstatic
python manage.py cleanpyc
touch main_site/wsgi.py