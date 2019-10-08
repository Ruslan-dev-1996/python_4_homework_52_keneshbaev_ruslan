from django.contrib import admin
from webapp.models import Tracker, Status, Type
class TrackerAdmin(admin.ModelAdmin):
        list_display = ['pk', 'summary', 'description', 'status', 'type', 'created_at']
        list_filter = ['summary', 'status', 'type']
        list_display_links = ['pk', 'summary']
        search_fields = ['summary', 'description']
        exclude = []
        readonly_fields = ['created_at']

admin.site.register(Tracker, TrackerAdmin)
admin.site.register(Status)
admin.site.register(Type)
