from django.contrib import admin
from .models import Movie, Rater, Rating


class RaterAdmin(admin.ModelAdmin):
    pass


class MovieAdmin(admin.ModelAdmin):
    pass


class RatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
