from django.db import models
from django.db.models import Avg, Sum

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    number_ratings = models.IntegerField(default=-1)
    rating_sum = models.IntegerField(default=-1)
    average_rating = models.FloatField()


# def populate_sum_column(apps, schema_editor):
#     movies = Movie.objects.all()
#     for movie in movies:
#         if movie.number_ratings == 0:
#             movie.rating_sum = 0
#             movie.save()
#         else:
#             avg_ratings = movie.rating_set.all().aggregate(Avg('stars'))
#             movie.average_rating = avg_ratings['stars__avg']
#             movie.save()





    def __str__(self):
        return self.title


    # def load_movie_data():
    #
    #     with open('/Users/JonathanKross/tiy/assignments/django-movies/ml-1m/movies.dat', encoding='windows-1252') as f:
    #         reader = csv.DictReader([line.replace('::', '\t') for line in f],
    #         fieldnames='MovieID::Title::Genres'.split('::'),
    #         delimiter='\t'
    #         )
    #
    #     for row in reader:
    #         m = Movie(title=row['Title'], genre=row['Genres'])
    #         m.save()

    # @staticmethod
    # def get_average_rating(minimum_ratings=300):
    #     movies = Movie.objects.all()
    #     average_ratings = []
    #     for movie in movies:
    #         ratings = movie.rating_set.all()
    #         if len(ratings) >= minimum_ratings:
    #             average_ratings.append((movie.title, ratings.aggregate(Avg('stars'))))
    #     return average_ratings, len(average_ratings)

class Rater(models.Model):

    GENDER_CHOICES = (('M', 'Male'),
                    ('F', 'Female')
                    )

    AGE_CHOICES = ((1, 'Under 18'),
                (18, '18-24'),
                (25, '25-34'),
                (35, '35-44'),
                (45, '45-49'),
                (50, '50-55'),
                (56, '56+')
                )

    OCCUPATION_CHOICES = ((0, "Other"),
                        (1, "Academic/Educator"),
                        (2, "Artist"),
                        (3, "Clerical/Admin"),
                        (4, "College/Grad Student"),
                        (5, "Customer Service"),
                        (6, "Doctor/Health Care"),
                        (7, "Executive/Managerial"),
                        (8, "Farmer"),
                        (9, "Homemaker"),
                        (10, "K-12 Student"),
                        (11, "Lawyer"),
                        (12, "Programmer"),
                        (13, "Retired"),
                        (14, "Sales/Marketing"),
                        (15, "Scientist"),
                        (16, "Self-employed"),
                        (17, "Technician/Engineer"),
                        (18, "Tradesman/Craftsman"),
                        (19, "Unemployed"),
                        (20, "Writer")
                        )

    age = models.IntegerField(choices=AGE_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES)
    zipcode = models.CharField(max_length=10)


    def __str__(self):
        return str(self.id)


    # def load_user_data():
    #
    #     with open('/Users/JonathanKross/tiy/assignments/django-movies/ml-1m/users.dat') as f:
    #         reader = csv.DictReader([line.replace('::', '\t') for line in f],
    #         fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
    #         delimiter='\t'
    #         )
    #
    #     for row in reader:
    #         r = Rater(gender=row['Gender'], age=row['Age'],
    #             occupation=row['Occupation'], zipcode=row['Zip-code'])
    #         r.save()


class Rating(models.Model):
    rater = models.ForeignKey('Rater')
    movie = models.ForeignKey('Movie')
    stars = models.IntegerField()

    def __str__(self):
        return 'Rating(id={}, rater={}, stars={}, movie={})'.format(
            self.id, self.rater, self.stars, self.movie)


    # def load_rating_data():
    #
    #     with open('/Users/JonathanKross/tiy/assignments/django-movies/ml-1m/ratings.dat') as f:
    #         reader = csv.DictReader([line.replace('::', '\t') for line in f],
    #         fieldnames='UserID::MovieID::Rating::Timestamp'.split('::'),
    #         delimiter='\t'
    #         )
    #
    #     for row in reader:
    #         r = Rating(rater=Rater.objects.get(id=row['UserID']),
    #                     movie=Movie.objects.get(id=row['MovieID']),
    #                     stars=row['Rating'])
    #         r.save()
