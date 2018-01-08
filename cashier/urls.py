from django.conf.urls import patterns, url
from django.contrib import admin
from cashier import views

urlpatterns = [
    url(r'^$', views.FAList.as_view() , name = "list"),
    url(r'^create/$', views.FACreate.as_view(), name = 'create'),
    url(r'^edit/(?P<id>\d+)', views.FAUpdate.as_view(), name = 'edit'),
    url(r'^delete/(?P<id>\d+)', views.FADelete.as_view(), name = 'delete'),

]