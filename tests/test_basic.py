import os
import subprocess

#from .. import main_site
#from .. import ng


def test_basic():
	assert True

def test_secretkey():
	from main_site import secretkey
	SECRET_KEY = secretkey.SECRET_KEY
	assert len(SECRET_KEY) == 50

def test_messages():
	os.chdir('ng')
	cmd = 'django-admin makemessages -l fr -e js,html,py'
	subprocess.check_output(cmd.split(' '))
	with open('locale/fr/LC_MESSAGES/django.po','r') as f:
		ans = f.read()
	assert len(ans.split('fuzzy')) == 2
	assert len(ans.split('""\n\n')) == 1
