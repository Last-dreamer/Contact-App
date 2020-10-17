from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

from . import models


class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'gender', 'email', 'info', 'phone')
    list_editable = ('info',)
    list_display_links = ('id', 'name')
    list_per_page = 10
    search_fields = ('name', 'gender', 'info', 'phone', 'email')
    list_filter = ('gender', 'date',)


admin.site.register(models.Contact, ContactAdmin)
admin.site.unregister(Group)
