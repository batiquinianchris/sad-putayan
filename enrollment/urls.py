from django.conf.urls import patterns, url
from django.contrib import admin
from enrollment import views

urlpatterns = [
    url(r'^$', views.SectionList.as_view() , name = "list"),
    url(r'^create/$', views.SectionCreate.as_view(), name = 'create'),
    url(r'^edit/(?P<id>\d+)', views.SectionUpdate.as_view(), name = 'edit'),
    url(r'^delete/(?P<id>\d+)', views.SectionDelete.as_view(), name = 'delete'),

]