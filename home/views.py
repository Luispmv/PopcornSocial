# home/views.py
from django.shortcuts import render
from reviews.models import Review
from movies.models import Movie

def home(request):
    # Obtener las 10 reseñas más recientes
    reviews = Review.objects.all().order_by('-created_at')[:10]
    
    # Preparar las estrellas de calificación
    for review in reviews:
        review.stars = '★' * review.rating + '☆' * (5 - review.rating)
    
    # Obtener las primeras 10 películas
    movies = Movie.objects.all()[:10]
    
    return render(request, 'home.html', {
        'reviews': reviews,
        'movies': movies
    })