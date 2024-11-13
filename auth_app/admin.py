from django.contrib import admin

from auth_app.models import LoginTable, UserRegistration

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(UserRegistration)