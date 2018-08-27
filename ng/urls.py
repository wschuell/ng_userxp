from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404, handler500
import django

from . import views

from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/ng/img/favicon.ico', permanent=True)


app_name = 'ng'
urlpatterns = [
    url(r'^favicon\.ico$', favicon_view),
    #url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^new_experiment/$', views.new_experiment, name='new_experiment'),
    #url(r'^choose_experiment/$', views.choose_experiment, name='choose_experiment'),
    url(r'^new_experiment/(?P<xp_cfg_name>[0-9a-z]+)$', views.new_experiment, name='new_experiment_cfg'),
    #url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.exp_resume, name='exp_resume'),
    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/results_srtheo/$', views.result_srtheo, name='results_srtheo'),#ResultsView.as_view(), name='results'),
    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-hearer-(?P<meaning>[0-9a-z]+)/results/$', views.result_hearer, name='results_hearer'),#ResultsView.as_view(), name='results'),
     url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-speaker-(?P<meaning>[0-9a-z]+)-(?P<word>[0-9a-z]+)/results/$', views.result_speaker, name='results_speaker'),#ResultsView.as_view(), name='results'),
    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-hearer-$', views.result_hearer, name='results_hearer_base'),#ResultsView.as_view(), name='results'),
     url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-speaker-$', views.result_speaker, name='results_speaker_base'),#ResultsView.as_view(), name='results'),
    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/vote/$', views.vote, name='vote'),
    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/continue/$', views.continue_userxp, name='continue'),
    #url(r'^accounts/login/$', django.contrib.auth.views.login,name='login_old'),
    url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': '/ng/login'}, name='logout'),
    #url(r'^login/$', views.login_view, name='login'),
    url(r'^login/$', views.get_name, name='login'),

    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-hearer-(?P<meaning>[0-9a-z]+)/results_json/$', views.result_hearer_json, name='results_hearer_json'),#ResultsView.as_view(), name='results'),

     url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-speaker-(?P<meaning>[0-9a-z]+)-(?P<word>[0-9a-z]+)/results_json/$', views.result_speaker_json, name='results_speaker_json'),#ResultsView.as_view(), name='results'),

    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-hearer-(?P<meaning>[0-9a-z]+)/results_continue/$', views.result_hearer_continue, name='results_hearer_continue'),#ResultsView.as_view(), name='results'),
     url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-speaker-(?P<meaning>[0-9a-z]+)-(?P<word>[0-9a-z]+)/results_continue/$', views.result_speaker_continue, name='results_speaker_continue'),#ResultsView.as_view(), name='results'),


    url(r'^results_inner/(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/(?P<bool_succ>(True|False))/$', views.result_inner, name='results_inner'),#ResultsView.as_view(), name='results'),
    url(r'^results_inner/(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.result_inner, name='results_inner_base'),#ResultsView.as_view(), name='results'),
     url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-speaker-(?P<meaning>[0-9a-z]+)-(?P<word>[0-9a-z]+)/results_json/$', views.result_speaker_json, name='results_speaker_json'),#ResultsView.as_view(), name='results'),


    url(r'^$',views.home,name='home'),

    url(r'^test/$',views.test,name='test'),
    url(r'^accounts/profile/$', views.new_experiment, name='new_experiment_2'),
    #url(r'^accounts/login/$', auth_views.LoginView.as_view()),

    url(r'^userinfo_$', views.none, name='send_user_info_base'),
    url(r'^userinfo_(?P<username>[\w-]+)$', views.create_and_login, name='send_user_info'),

	######
	url(r'^story$', views.story, name='story'),
	url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/results', views.score, name='results'),
    url(r'^infos', views.info, name='info'),
]

handler404 = views.error
handler500 = views.error

"""
    ###DEBUG###

    url(r'^test_score', views.test_score, name='test_score'),
    url(r'^test_infos', views.test_info, name='test_info'),
    url(r'^error', views.error, name="error"),
"""
