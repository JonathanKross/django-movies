from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^top_movies/$', views.top_movies, name='top_movies'),
    url(r'^movies/(?P<movie_id>\d+)$', views.show_movie, name='rater_detail'),
    url(r'^raters/(?P<rater_id>\d+)$', views.show_rater, name='movie_detail'),
]
