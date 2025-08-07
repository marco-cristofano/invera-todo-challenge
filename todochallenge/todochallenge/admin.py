from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class TodoChallengeAdminSite(admin.AdminSite):
    site_header = 'Administrador de TodoChallenge'
    site_title = 'Administrador de TodoChallenge'
    index_title = 'TodoChallenge administrador'


admin_site = TodoChallengeAdminSite(name="simcoadminsite")
admin_site.register(User, UserAdmin)
