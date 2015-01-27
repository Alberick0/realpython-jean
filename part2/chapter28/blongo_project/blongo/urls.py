__author__ = 'alberick'
from django.conf.urls import patterns, url
from blongo import views

urlpatterns = patterns('blong.views',
                       url(r'^$', views.index, name='index'),
                       )
