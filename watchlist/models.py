from django.db import models
from users.models import CustomUser
from movies.models import Movie

# Create your models here.
class WatchlistItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pendiente'),
        ('WATCHING', 'Viendo'),
        ('COMPLETED', 'Completada')
    ])