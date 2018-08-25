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
	models.UserNG,
]



from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

#UserAdmin.list_display = ('username','email', 'first_name', 'last_name', 'is_active', 'date_joined', 'last_login', 'is_staff')

#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)

from .admin_bis import *

class MeaningAdmin(admin.ModelAdmin):
	readonly_fields = ('meaning', 'meaning')

class WordAdmin(admin.ModelAdmin):
	readonly_fields = ('word', 'word')

class ScoreAdmin(admin.ModelAdmin):
	readonly_fields = (
	'user',
	'experiment',
	'score'
	)
	list_display = ('user', 'score')

class UserNGInline(admin.StackedInline):
	model = models.UserNG
	can_delete = False
	list_display = ('nbr_won','nbr_played')

class UserAdmin(BaseUserAdmin):
	inlines = (UserNGInline, )

class ExperimentAdmin(admin.ModelAdmin):

	readonly_fields=(
	'xp_uuid',
	'user',
	'user_agent_uuid',
	'xp_config',
	'is_complete',
	'max_interaction',
	'interaction_counter',
	'words',
	)
	exclude = (
	'exit_value',
	'meanings',
	'last_ms',
	'last mh',
	'last_w',
	'last_role',
	'last_bool_succ',
	'last_nb_skipped',
	'last_mh',
	'size',
	)
	list_display = ('user', 'created_at', 'xp_uuid', 'before_info', 'is_complete', 'max_interaction','game_won',)
	list_filter = ('user', 'max_interaction')

class NewUserAdmin(admin.ModelAdmin):

	readonly_fields=(

	)
	exclude = (

	)
	list_display = ('first_name', 'created_at', 'updated_at', 'code', 'tuto_played', 'nbr_won', 'nbr_played', 'q_seen', 'q_filled','prolific_user','use_matomo')
	list_filter = ('user',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(models.UserNG, NewUserAdmin)
admin.site.register(models.Experiment, ExperimentAdmin)
admin.site.register(models.Score, ScoreAdmin)
admin.site.register(models.Meaning, MeaningAdmin)
admin.site.register(models.Word, WordAdmin)
