from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    synopsis = models.TextField()
    duration = models.IntegerField()  # in minutes
    cast = models.TextField()
    release_date = models.DateField()
    categories = models.ManyToManyField(Category)
    poster = models.ImageField(upload_to='movie_posters/')