from atexit import register
from django.contrib import admin
from .models import Shops

admin.site.register(Shops)
