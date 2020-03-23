from django.contrib import admin

from .models import Matter
from .models import Mood
# Register your models here.

@admin.register(Matter)
class MatterAdmin(admin.ModelAdmin):
    fields = ('nickname', 'message', 'del_pass')
    list_display = ('nickname', 'mood', 'pub_time',)

@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    fields = ('status',)

    list_display = ('status',)