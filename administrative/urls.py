from django.conf.urls import patterns, url
from django.contrib import admin
from administrative import views

urlpatterns = [
    url(r'^$', views.EmployeeList.as_view() , name = "list"),
    url(r'^create/$', views.EmployeeCreate.as_view(), name = 'create'),
    url(r'^edit/(?P<id>\d+)', views.EmployeeUpdate.as_view(), name = 'edit'),
    url(r'^delete/(?P<id>\d+)', views.EmployeeDelete.as_view(), name = 'delete'),

]