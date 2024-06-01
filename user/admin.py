from django.contrib import admin
from .models import UserProfile
# Register your models here.
from django.contrib.auth.admin import UserAdmin

class ProfileAdmin(UserAdmin):
    pass

admin.site.register(UserProfile, ProfileAdmin)