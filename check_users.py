from django.contrib.auth.models import User
import os
import json
import random
import string

def random_string(N):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

if not os.path.exists('superusers.json'):
	superusers = {random_string(6):random_string(20)}
	with open('superusers.json','w') as f:
		f.write(json.dumps(superusers))
else:
	with open('superusers.json','r') as f:
		superusers = json.loads(f.read())

for username,password in list(superusers.items()):
	if not User.objects.filter(username=username):
		User.objects.create_superuser(username, '', password).save()
