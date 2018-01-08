from django.conf.urls import patterns, url
from django.contrib import admin
from registrar import views

urlpatterns = [
    url(r'^$', views.SHS_SubjList.as_view() , name = "list"),
    url(r'^create/$', views.SHS_SubjCreate.as_view(), name = 'create'),
    url(r'^edit/(?P<id>\d+)', views.SHS_SubjUpdate.as_view(), name = 'edit'),
    url(r'^delete/(?P<id>\d+)', views.SHS_SubjDelete.as_view(), name = 'delete'),

]