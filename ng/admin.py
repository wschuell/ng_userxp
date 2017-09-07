# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models 
# Register your models here.
from django_smart_autoregister import auto_configure_admin_for_model
from django_smart_autoregister import auto_configure_admin


models_list = [
	models.Experiment,
	models.XpConfig,
	models.Meaning,
	models.Word,
	models.CookieId,
	models.Score,
	models.Role,
	models.PastInteraction,
]

for m in models_list:
	auto_configure_admin_for_model(m)
