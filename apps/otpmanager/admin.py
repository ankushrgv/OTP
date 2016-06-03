from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import KisanUser
# Register your models here.

class KisanAdmin(UserAdmin):
	fieldsets = (
		(
			None,{
				'fields':(
					'username',
					'password',
					'first_name',
					'last_name',
					'email',
					'is_active',
					'is_staff',
					'date_joined',
					'last_login',
					'phone_number'
				),
			}
		),
	)
	list_display = ['username', 'first_name', 'is_active', 'is_staff' ]


admin.site.register(KisanUser, KisanAdmin)