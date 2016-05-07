

def populate_sum_column(apps, schema_editor):
    movies = Movie.objects.all()
    for movie in movies:
        if movie.number_ratings == 0:
            movie.rating_sum = 0
            movie.save()
        else:
            avg_ratings = movie.rating_set.all().aggregate(Avg('stars'))
            movie.average_rating = avg_ratings['stars__avg']
            movie.save()


def load_movie_data():

    with open('/Users/JonathanKross/tiy/assignments/django-movies/ml-1m/movies.dat', encoding='windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
        fieldnames='MovieID::Title::Genres'.split('::'),
        delimiter='\t'
        )

    for row in reader:
        m = Movie(title=row['Title'], genre=row['Genres'])
        m.save()


@staticmethod
def get_average_rating(minimum_ratings=300):
    movies = Movie.objects.all()
    average_ratings = []
    for movie in movies:
        ratings = movie.rating_set.all()
        if len(ratings) >= minimum_ratings:
            average_ratings.append((movie.title, ratings.aggregate(Avg('stars'))))
    return average_ratings, len(average_ratings)


def load_user_data():

    with open('/Users/JonathanKross/tiy/assignments/django-movies/ml-1m/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
        fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
        delimiter='\t'
        )

    for row in reader:
        r = Rater(gender=row['Gender'], age=row['Age'],
            occupation=row['Occupation'], zipcode=row['Zip-code'])
        r.save()


def load_rating_data():

    with open('/Users/JonathanKross/tiy/assignments/django-movies/ml-1m/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
        fieldnames='UserID::MovieID::Rating::Timestamp'.split('::'),
        delimiter='\t'
        )

    for row in reader:
        r = Rating(rater=Rater.objects.get(id=row['UserID']),
                    movie=Movie.objects.get(id=row['MovieID']),
                    stars=row['Rating'])
        r.save()


def create_rater_users():
    raters = Rater.objects.all()
    for rater in raters:
        username = 'rater' + str(rater.id)
        email = 'rater' + str(rater.id) + '@raters.com'
        password = 'rater' + str(rater.id) + 'password'
        user = User.objects.create_user(username, email, password)
