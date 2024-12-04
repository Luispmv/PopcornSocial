from django.shortcuts import render
from .models import Review

def review_list(request):
    reviews = Review.objects.all()
    for review in reviews:
        review.stars = '★' * review.rating + '☆' * (5 - review.rating)
    return render(request, 'home.html', {'reviews': reviews})