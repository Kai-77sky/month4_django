from django.contrib import admin
from django.contrib.auth import authenticate, login
from .models import Bottle


admin.site.register(Bottle)
