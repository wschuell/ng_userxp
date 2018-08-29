docker exec -i ng /bin/bash -c "python manage.py shell" << 'EOF'
print("Cleaning locust data")
from django.contrib.auth.models import User
from ng.models import UserNG,Experiment,PastInteraction
ung_list = UserNG.objects.filter(code='locust_test')
u_list = [ung.user for ung in ung_list]
for u in u_list:
	print("Cleaning data for user : ",u.username)
	ung = UserNG.objects.filter(user=u)
	xp_list = Experiment.objects.filter(user=u)
	for xp in xp_list:
		print("Cleaning data for experiment : ",xp.xp_uuid)
		xp.delete()
	ung.delete()
	u.delete()
exit()
EOF