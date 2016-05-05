from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, movie_id):
    return HttpResponse("You're looking at question %s." % movie_id)

def results(request, movie_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % movie_id)

def vote(request, movie_id):
    return HttpResponse("You're voting on question %s." % movie_id)
