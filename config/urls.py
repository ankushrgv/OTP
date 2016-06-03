"""
otp URL Configuration

"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	
    url(r'^', include('apps.otpmanager.urls', namespace='otpmanager')),	
    url(r'^admin/', admin.site.urls),
]
