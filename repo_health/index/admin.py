"""
Hold a read only admin to be used across apps.
"""

from django.contrib import admin as a

class ReadOnlyAdmin(a.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]
