
DJANGO_MODULE_SETTINGS="main_site.production_settings"
export DJANGO_MODULE_SETTINGS
python manage.py makemigrations ng
python manage.py migrate
python manage.py collectstatic --noinput