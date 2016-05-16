# Django MovieLens 1M Database Website

### A Website to see Top Movies, Movie Info, and User Info from the MovieLens 1M Database

* `localhost/lensview/` shows the lensview app homepage
* `localhost/lensview/top_movies` shows the top rated 20 movies with over 300 reviews
* `localhost/lensview/movies/movie_id` for each movie's page
* `localhost/lensview/raters/rater_id` for each rater's page

### System Requirements

* You will need to have **Python&nbsp;3** installed on your machine.

* Copy this repo to your computer; the below assumes you have kept the default folder name as `movieratings`.

* You will need to make sure that you have a virtual environment running Python&nbsp;3 in the folder that you made in the above step. [See this site for details if you're not familiar.](http://docs.python-guide.org/en/latest/dev/virtualenvs/) **Complete this step before attempting the below.**

* Using your command line program, install the requirements file in your virtual environment: `pip install -r requirements.txt`.

* You will need to download the [MovieLens 1M](http://files.grouplens.org/datasets/movielens/ml-1m.zip) dataset. Unzip the downloaded file and move the folder into the same directory you cloned this repo. (One directory above the  directory containing `manage.py`). It should be named `ml-1m`.

* This app is set up to run on PostgreSQL. I have set it up to have a database named `movies`. The database name, user, and password can all be configured to your preferences in the `/movieratings/movieratings/settings.py` file. If you do not have PostgreSQL on your machine.

* Direct message me to receive the SECRET_KEY needed to run this Django app.

* **To load the data**, you will need to run some shell commands. Navigate to the `movieratings/movieratings` folder and confirm that you see the `manage.py` file. Then run the following line (this step will probably take at least an hour to load all the data):
```
$ python manage.py migrate
```

* **Running the site** requires more command line. Navigate to `movieratings/movieratings` and enter `python manage.py runserver` This will take over the current command-line program's window. To kill the process press `Ctrl+C` or quit the command-line program entirely.

### Movie Pages
Located at `localhost/lensview/movies/movie_id`, where `localhost` is the location of your django server and `movie_id` is the actual movie id in the database.

### Rater Pages
Located at `localhost/lensview/raters/rater_id`, where `localhost` is the location of your django server and `rater_id` is the actual movie id in the database.

### Top 20 Page
Located at `localhost/lensview/top_movies`, where `localhost` is the location of your django server. Shows the top 20 movies by average rating.

### Homepage
Located at `localhost/lensview/`, where `localhost` is the location of your django server. Shows the ability to register as a new user or login as a previously register rater.

* To view a pre-registered rater: username = raterIDNUMBER, where IDNUMBER is any number from 1-6041. password = raterIDNUMBERpassword, where IDNUMBER is any number from 1-6041 and matches the number used in the username. 
