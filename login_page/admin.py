from django.contrib import admin
from login_page.models import *


# Register your models here.

class LoginAdmin(admin.ModelAdmin):
    display = 'username'

admin.site.register(LoginModels, LoginAdmin)


class SignupAdmin(admin.ModelAdmin):
    details = ('name', 'email')

admin.site.register(SignupModel, SignupAdmin)