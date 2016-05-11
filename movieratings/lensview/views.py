from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Movie, Rater, Rating
from .forms import UserForm, RatingForm
from django.views.generic.detail import DetailView


def index(request):
    return render(request, "lensview/index.html")


def detail(request, movie_id):
    return HttpResponse("You're looking at movie %s." % movie_id)


def top_movies(request):
    significantly_rated = Movie.objects.filter(number_ratings__gte=300)
    top_twenty = significantly_rated.order_by('average_rating').reverse()[:20]
    return render(request, 'lensview/top_movies.html', {'top_twenty': top_twenty})


def show_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    ratings = movie.rating_set.all()
    rating_list = Rating.objects.filter(movie_id=movie.id)
    rater_queries = rating_list.values_list('rater_id', flat=True)
    return render(request, 'lensview/movie.html', {'movie': movie, 'ratings': ratings, 'rater_queries': rater_queries})


# def show_rater(request, rater_id):
#     rater = get_object_or_404(Rater, pk=rater_id)
#     ratings = rater.rating_set.all()
#     return render(request, 'lensview/rater.html', {'rater': rater, 'ratings': ratings})


class RaterDetailView(DetailView):
    model = Rater

    def get_context_data(self, **kwargs):
        context = super(RaterDetailView, self).get_context_data(**kwargs)
        context['ratings'] = self.object.rating_set.all()
        return context


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


def new(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rater = Rater.objects.get(user=request.user)
            rating.rater = rater
            rating.save()
            return HttpResponseRedirect('/lensview/')
    else:
        form = RatingForm()
    return render(request, 'lensview/new.html', {'form': form})
