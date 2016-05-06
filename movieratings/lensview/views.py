from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Movie

def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, movie_id):
    return HttpResponse("You're looking at movie %s." % movie_id)

def top_movies(request):
    avg, avg_length = Movie.get_average_rating()
    return HttpResponse("This is a list of the top rated movies {}".format(avg_length))
