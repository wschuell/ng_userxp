#!/bin/bash

if [ "$1" != "nogit" ]
then
	git pull || exit 1
	bash update_ngal.sh || exit 1
fi;

(cd ng && python gen_json_str.py) || exit 1

(django-admin compilemessages &&

python manage.py makemigrations &&
python manage.py makemigrations auth &&
python manage.py makemigrations ng &&
python manage.py migrate auth &&
python manage.py migrate &&
python manage.py migrate ng &&
python manage.py collectstatic --noinput ) || exit 1

touch main_site/wsgi.py
