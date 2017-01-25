from django.contrib import admin as a
from .models import *

a.site.register(GhUser)
# class GhUserAdmin(a.ModelAdmin