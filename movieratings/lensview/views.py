from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie, Rater, Rating
from .forms import UserForm

def index(request):
    return render(request, "lensview/index.html")


def detail(request, movie_id):
    return HttpResponse("You're looking at movie %s." % movie_id)


def top_movies(request):
    significantly_rated = Movie.objects.filter(number_ratings__gte=300)
    top_twenty = significantly_rated.order_by('average_rating').reverse()[:20]
    return render(request, 'lensview/top_movies.html', {'top_twenty': top_twenty})


def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    ratings = movie.rating_set.all()
    return render(request, 'lensview/movie.html', {'movie': movie, 'ratings': ratings})


def show_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = rater.rating_set.all()
    return render(request, 'lensview/rater.html', {'rater': rater, 'ratings': ratings})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print (user_form.errors)
    else:
        user_form = UserForm()
    return render(request,
            'registration/register.html',
            {'user_form': user_form, 'registered': registered} )
