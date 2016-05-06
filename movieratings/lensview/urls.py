from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^top_movies/$', views.top_movies, name='top_movies'),
]
