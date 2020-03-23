from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'sex', 'height', 'created_date']

@admin.register(ProUser)
class ProUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'sex', 'height']


