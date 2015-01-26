__author__ = 'alberick'

from django.conf.urls import patterns, url
from movie_suggest import views

urlpatterns = patterns(
    'movie_suggest.views',
    url(r'^$', views.index, name='index'),
    # url(r'^pulser/', views.pulser, name='pulser'),
)