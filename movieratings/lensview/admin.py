from django.contrib import admin
from .models import Movie, Rater, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'age', 'occupation', 'zipcode')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'genre', 'average_rating')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('rater','movie', 'stars')


admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
