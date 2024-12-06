from django.test import TestCase
# Create your tests here.
from django.contrib.auth.models import User
from movies.models import Movie
from .models import Review

class ReviewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.movie = Movie.objects.create(title='Test Movie', release_date='2023-01-01')

    def test_create_review(self):
        review = Review.objects.create(user=self.user, movie=self.movie, review_text='Great movie!', rating=5)
        self.assertEqual(review.review_text, 'Great movie!')
        self.assertEqual(review.rating, 5)

    def test_update_review(self):
        review = Review.objects.create(user=self.user, movie=self.movie, review_text='Great movie!', rating=5)
        review.review_text = 'Not so great movie!'
        review.rating = 3
        review.save()
        self.assertEqual(review.review_text, 'Not so great movie!')
        self.assertEqual(review.rating, 3)

    def test_delete_review(self):
        review = Review.objects.create(user=self.user, movie=self.movie, review_text='Great movie!', rating=5)
        review_id = review.id
        review.delete()
        with self.assertRaises(Review.DoesNotExist):
            Review.objects.get(pk=review_id)

    def test_review_str(self):
        review = Review.objects.create(user=self.user, movie=self.movie, review_text='Great movie!', rating=5)
        self.assertEqual(str(review), f"{self.movie.title} - {self.user.username}")