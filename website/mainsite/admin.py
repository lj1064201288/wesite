from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'enaled',)
    ordering = ('-created_date',)

@admin.register(PollItem)
class PollItemAdmin(admin.ModelAdmin):
    list_display = ('poll', 'name', 'image_url', 'vote',)
    ordering = ('poll',)


admin.site.register(VoteCheck)