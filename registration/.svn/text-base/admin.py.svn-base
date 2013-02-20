#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Use standard Django admin pages"

from django.contrib import admin
from django_logistics.registration.models import RegistrationProfile

class RegistrationAdmin(admin.ModelAdmin):
    "Set properties of the Admin"

    list_display = ('__unicode__', 'activation_key_expired')
    search_fields = ('user__username', 'user__first_name')


admin.site.register(RegistrationProfile, RegistrationAdmin)
