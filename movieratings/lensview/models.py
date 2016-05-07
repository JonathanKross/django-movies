from django.db import models
from django.db.models import Avg, Sum
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    number_ratings = models.IntegerField(default=-1)
    rating_sum = models.IntegerField(default=-1)
    average_rating = models.FloatField()


    def __str__(self):
        return self.title


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
    occupation = models.IntegerField(choices=OCCUPATION_CHOICES)
    zipcode = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return str(self.id)


class Rating(models.Model):
    rater = models.ForeignKey('Rater')
    movie = models.ForeignKey('Movie')
    stars = models.IntegerField()

    def __str__(self):
        return 'Rating(id={}, rater={}, stars={}, movie={})'.format(
            self.id, self.rater, self.stars, self.movie)
