import os


from .. import main_site
from .. import ng


def test_basic():
	assert True

def test_secretkey():
	from ..main_site import secretkey
	SECRET_KEY = secretkey.SECRET_KEY
	assert len(SECRET_KEY) == 50

