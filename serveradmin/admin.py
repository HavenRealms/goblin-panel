from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

# Register your models here.
admin.site.register(Location)
admin.site.register(Node)
admin.site.register(Allocation)
admin.site.register(Database)
admin.site.register(Hoarde)
admin.site.register(Gem)
admin.site.register(Server)
admin.site.register(Theme)
admin.site.register(UserProfile)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)