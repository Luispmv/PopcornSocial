from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)  # Título de la película
    description = models.TextField(blank=True)  # Descripción de la película
    release_date = models.DateField(null=True, blank=True)  # Fecha de lanzamiento
    genre = models.CharField(max_length=100, blank=True)  # Género de la película
    director = models.CharField(max_length=150, blank=True)  # Director de la película
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)  # Póster de la película
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación del registro

    def __str__(self):
        return self.title
