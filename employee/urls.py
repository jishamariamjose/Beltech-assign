from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import * 

#urlpatterns to fetch below urls
#http://127.0.0.1:8000/employees
#http://127.0.0.1:8000/employees/?chunk=3
urlpatterns = [
    url(r'^employees$', views.employee_list, name='employee_list'),
    #url(r'^employees/(?P<pk>.*)$', views.employee_detail, name='employee_detail'),
    url(r'^employees/$', views.employee_detail_new, name='employee_detail_new'),
]

