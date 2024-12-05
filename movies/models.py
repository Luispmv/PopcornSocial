from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nombre del género

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)  # Título de la película
    description = models.TextField(blank=True)  # Descripción de la película
    release_date = models.DateField(null=True, blank=True)  # Fecha de lanzamiento
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True, related_name='movies')  # Relación con géneros
    director = models.CharField(max_length=150, blank=True)  # Director de la película
    poster_url = models.URLField(blank=True, null=True)  # URL de la imagen de la película
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación del registro

    def __str__(self):
        return self.title