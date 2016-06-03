from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


## Model for Contacts

class KisanUser(AbstractUser):
	phone_number = models.CharField(max_length=10)
	otp_count = models.IntegerField(default=0)

	def __unicode__(self):
		return self.first_name


## Model for SMS

class Message(models.Model):
	kisan_user = models.ForeignKey(KisanUser, related_name='kisanuser') 
	otp = models.IntegerField(default=0)
	msg = models.CharField(max_length=30, default='Hi')
	sent_time = models.DateTimeField(auto_now=True, auto_now_add=False)
	status = models.CharField(max_length=20, default='Failed')

	def __unicode__(self):
		return self.otp
