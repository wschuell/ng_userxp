

echo 'NG_USERXP_DEV_MODE:'$NG_USERXP_DEV_MODE

if [ $NG_USERXP_DEV_MODE -eq 2 ]
then
	export DJANGO_MODULE_SETTINGS="main_site.production_settings"
	echo 'settings:'$DJANGO_MODULE_SETTINGS
fi;


service postgresql restart &&
sleep 10 &&
python manage.py makemigrations &&
python manage.py migrate &&
python manage.py collectstatic --noinput && 

echo "from django.contrib.auth.models import User; User.objects.all() or User.objects.create_user('admin', 'admin@example.com', 'password').save(); exit();" | python manage.py shell &&

if [ $NG_USERXP_DEV_MODE -eq 0 ]
then
	bash gunicorn_script.sh;
else
	python manage.py runserver 0.0.0.0:8000 --settings=$DJANGO_MODULE_SETTINGS
fi;
