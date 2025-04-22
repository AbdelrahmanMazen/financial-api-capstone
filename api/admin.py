from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Transaction

# Avoid re-registering the User model
try:
    admin.site.unregister(User)  # Unregister if already registered
except admin.sites.NotRegistered:
    pass

admin.site.register(Transaction)
admin.site.register(User, UserAdmin)  # Register the User model