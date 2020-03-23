from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    ordering = ('-created_at',)

@admin.register(PollItem)
class PollItemAdmin(admin.ModelAdmin):
    list_display = ('poll', 'name', 'vote', )



admin.site.register(VoteCheck)