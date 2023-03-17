from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile


# Description to insert in the admin interface
class ProfileInlined(admin.TabularInline):
    model = Profile
    can_delete = False


# Define the UserAdmin class
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInlined,)


# Register UserAdmin
# This will allow us to use the admin site with the added fields instead of the default version
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
