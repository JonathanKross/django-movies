from django.shortcuts import render
from lensview.models import Rater, Rating, Movie
from django.contrib.auth.models import User

def profile(request):
    rater = Rater.objects.get(user_id=request.user.id)
    ratings = rater.rating_set.all()
    return render(request, 'accounts/profile.html', {'rater': rater, 'ratings': ratings})
