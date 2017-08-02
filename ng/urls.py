from django.conf.urls import url
from django.contrib.auth import views as auth_views
import django

from . import views


app_name = 'ng'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new_experiment/$', views.new_experiment, name='new_experiment'),
    #url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.testdet, name='detail'),
    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/results_srtheo/$', views.result_srtheo, name='results_srtheo'),#ResultsView.as_view(), name='results'),
    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-hearer-(?P<meaning>[0-9a-z]+)/results/$', views.result_hearer, name='results_hearer'),#ResultsView.as_view(), name='results'),
     url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-speaker-(?P<meaning>[0-9a-z]+)-(?P<word>[0-9a-z]+)/results/$', views.result_speaker, name='results_speaker'),#ResultsView.as_view(), name='results'),
    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-hearer-$', views.result_hearer, name='results_hearer_base'),#ResultsView.as_view(), name='results'),
     url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-speaker-$', views.result_speaker, name='results_speaker_base'),#ResultsView.as_view(), name='results'),
    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/vote/$', views.vote, name='vote'),
    url(r'^(?P<xp_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/continue/$', views.continue_userxp, name='continue'),
    url(r'^accounts/login/$', django.contrib.auth.views.login,name='login'),
    url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': '/ng/accounts/login'}, name='logout'),  

    
    url(r'^accounts/profile/$', views.new_experiment, name='new_experiment_2'),
    #url(r'^accounts/login/$', auth_views.LoginView.as_view()),
]
