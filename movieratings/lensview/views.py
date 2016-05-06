from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Movie

def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, movie_id):
    return HttpResponse("You're looking at movie %s." % movie_id)

def top_movies(request):
    significantly_rated = Movie.objects.filter(number_ratings__gte=300)
    top_twenty = significantly_rated.order_by('average_rating').reverse()[:20]
    return render(request, 'lensview/top_movies.html', {'top_twenty': top_twenty})
