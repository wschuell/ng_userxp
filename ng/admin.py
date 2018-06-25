# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models
# Register your models here.
#from django_smart_autoregister import auto_configure_admin_for_model
#from django_smart_autoregister import auto_configure_admin


models_list = [
	models.Experiment,
	models.XpConfig,
	models.Meaning,
	models.Word,
	models.CookieId,
	models.Score,
	models.Role,
	models.PastInteraction,
	models.Agent,
]



from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

#UserAdmin.list_display = ('username','email', 'first_name', 'last_name', 'is_active', 'date_joined', 'last_login', 'is_staff')

#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)

from .admin_bis import *
