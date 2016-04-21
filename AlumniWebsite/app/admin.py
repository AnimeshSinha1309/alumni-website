from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from app import models

class AlumnusInline(admin.StackedInline):
    model = models.Alumnus
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (AlumnusInline, )

class WorkplaceAdmin(admin.ModelAdmin):
    model = models.Workplace

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(models.Workplace, WorkplaceAdmin)