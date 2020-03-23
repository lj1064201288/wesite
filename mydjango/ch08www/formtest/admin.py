from django.contrib import admin

from .models import *

# Register your models here.




class PostAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'message', 'enabled', 'pub_time']
    list_per_page = 10

    ordering = ('-pub_time', )

admin.site.register(Post, PostAdmin)
admin.site.register(Mood)