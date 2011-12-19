from django.contrib import admin

from broadcasts.models import BroadcastMessage
from broadcasts.forms import BroadcastMessageForm


class BroadcastAdmin(admin.ModelAdmin):
    """Admin class for the broadcast messages"""
    form = BroadcastMessageForm
    list_display = ('message', 'start_time', 'end_time', 'is_published')
    list_filter = ('is_published',)
    search_fields = ['message']


admin.site.register(BroadcastMessage, BroadcastAdmin)
