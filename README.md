### Install this repo:

git clone https://github.com/wschuell/ng_userxp.git


### Install the naming games lib:

sudo pip install -e git+https://github.com/flowersteam/naminggamesal.git@develop#egg=naminggamesal

### Istall django:

sudo pip install django


### Move into the right folder:

cd ng_userxp 


### Create database etc:

python manage.py makemigrations ng && python manage.py migrate


### Create a user:

python manage.py shell

from django.contrib.auth.models import User

user=User.objects.create_user('USERNAME', password='PASSWORD')

user.save()


### Run server:

python manage.py runserver


### Play the game:

go to http://127.0.0.1:8000/ng

