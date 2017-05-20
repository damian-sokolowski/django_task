# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users_list.models import UserProfile


class UserInline(admin.StackedInline):
    model = UserProfile
    list_display = ('birthday', 'random_number',)
    can_delete = False
    verbose_name_plural = 'users profile'


class UserAdmin(BaseUserAdmin):
    inlines = (UserInline, )


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('birthday', 'random_number')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

