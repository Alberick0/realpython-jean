__author__ = 'alberick'
from django.conf.urls import patterns, include, url
from pulse import views

urlpatterns = patterns(
    'pulse.views',
    url(r'^$', views.index, name='index'),
    url(r'^pulser/', views.pulser, name='pulser'),
)
