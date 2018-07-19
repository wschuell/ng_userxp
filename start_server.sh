

echo 'NG_USERXP_DEV_MODE:'$NG_USERXP_DEV_MODE

if [ $NG_USERXP_DEV_MODE -eq 2 ]
then
	export DJANGO_MODULE_SETTINGS="main_site.production_settings"
	echo 'settings:'$DJANGO_MODULE_SETTINGS
fi;

rm ng/admin_bis.py
touch ng/admin_bis.py

#service postgresql restart &&
# while ! pg_isready > /dev/null 2> /dev/null; do
#   echo "Waiting for database to start"
#   sleep 1
# done &&

bash update_ngal.sh

#echo $(python manage.py admin_generator ng '^exp')
#python manage.py admin_generator ng >> ng/admin_bis.py &&
python manage.py makemigrations &&
python manage.py makemigrations auth &&
python manage.py makemigrations ng &&
python manage.py migrate auth &&
python manage.py migrate &&
python manage.py migrate ng &&
python manage.py collectstatic --noinput &&

echo "from django.contrib.auth.models import User; User.objects.all() or User.objects.create_user('admin', 'admin@example.com', 'password').save(); exit();" | python manage.py shell &&

if [ $NG_USERXP_DEV_MODE -eq 0 ]
then
	bash gunicorn_script.sh;
else
	if [ $NG_USERXP_DEV_MODE -eq 1 ]
	then
		python manage.py runserver 0.0.0.0:8000 --settings=$DJANGO_MODULE_SETTINGS;
	else
		echo 'Server started in testing mode: exiting'
		exit 0
	fi;
fi;
