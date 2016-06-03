import sys
import os

ROOT_FOLDER = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
if ROOT_FOLDER not in sys.path:
	sys.path.insert(1, ROOT_FOLDER + '/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

import django
django.setup()

from apps.otpmanager.models import KisanUser
import json

with open('/home/ankush/kisan_assignment/otp/static/json/contacts.json') as f:
	
	for line in f:
		
		doc = json.loads(line)
		f_name = doc.get('first_name')
		l_name = doc.get('last_name')
		ph_number = doc.get('phone_number')
		u_name = doc.get('username')
		u_password = doc.get('password')
		
		KisanUser.objects.create(
			username = u_name,
			password = u_password,
			first_name = f_name,
			last_name = l_name,
			phone_number = ph_number
			)