from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Movie, Genre
from datetime import date

from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Genre, Movie

class GenreTestCase(TestCase):
    def test_create_genre(self):
        genre = Genre.objects.create(name='Action')
        self.assertEqual(genre.name, 'Action')

    def test_genre_str(self):
        genre = Genre.objects.create(name='Action')
        self.assertEqual(str(genre), 'Action')

class MovieTestCase(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name='Action')

    def test_create_movie(self):
        movie = Movie.objects.create(
            title='Test Movie',
            description='A test movie description',
            release_date='2023-01-01',
            genre=self.genre,
            director='Test Director',
            poster_url='http://example.com/poster.jpg'
        )
        self.assertEqual(movie.title, 'Test Movie')
        self.assertEqual(movie.genre, self.genre)

    def test_update_movie(self):
        movie = Movie.objects.create(
            title='Test Movie',
            description='A test movie description',
            release_date='2023-01-01',
            genre=self.genre,
            director='Test Director',
            poster_url='http://example.com/poster.jpg'
        )
        movie.title = 'Updated Movie'
        movie.save()
        self.assertEqual(movie.title, 'Updated Movie')

    def test_delete_movie(self):
        movie = Movie.objects.create(
            title='Test Movie',
            description='A test movie description',
            release_date='2023-01-01',
            genre=self.genre,
            director='Test Director',
            poster_url='http://example.com/poster.jpg'
        )
        movie_id = movie.id
        movie.delete()
        with self.assertRaises(Movie.DoesNotExist):
            Movie.objects.get(pk=movie_id)

    def test_movie_str(self):
        movie = Movie.objects.create(
            title='Test Movie',
            description='A test movie description',
            release_date='2023-01-01',
            genre=self.genre,
            director='Test Director',
            poster_url='http://example.com/poster.jpg'
        )
        self.assertEqual(str(movie), 'Test Movie')