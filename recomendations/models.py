from django.db import models
from users.models import CustomUser
from movies.models import Movie

# Create your models here.
class UserWatchHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watched_date = models.DateTimeField(auto_now_add=True)

class Recommendation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    recommendation_score = models.FloatField()
    generated_at = models.DateTimeField(auto_now_add=True)