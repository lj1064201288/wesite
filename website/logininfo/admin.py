from django.contrib import admin
from .models import *

from .models import CustomUser

@admin.register(CustomUser)
class CustonUserAdmin(admin.ModelAdmin):
    list_display = ['username']
# Register your models here.

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = [ 'name',]
#
# @admin.register(Profile)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['user', 'height',]

@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ['status']
