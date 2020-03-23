from django.contrib import admin

from .models import *

# Register your models here.



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'message', 'enabled', 'pub_time']
    list_per_page = 10

    ordering = ('-pub_time', )

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'enabled']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mood)
