import os
def test_basic():
	assert True

def test_import():
	from .. import main_site
	from .. import ng

def test_secretkey():
	SECRET_KEY = main_site.secretkey.SECRET_KEY
	assert len(SECRET_KEY) == 50

