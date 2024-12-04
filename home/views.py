# home/views.py
from django.shortcuts import render
from reviews.models import Review

def home(request):
    # Obtener las 10 reseñas más recientes
    reviews = Review.objects.all().order_by('-created_at')[:10]
    
    # Preparar las estrellas de calificación
    for review in reviews:
        review.stars = '★' * review.rating + '☆' * (5 - review.rating)
    
    return render(request, 'home.html', {'reviews': reviews})