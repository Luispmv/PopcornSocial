from django.shortcuts import render
from .models import Review
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm
from movies.models import Movie

def review_list(request):
    reviews = Review.objects.all()
    for review in reviews:
        review.stars = '★' * review.rating + '☆' * (5 - review.rating)
    return render(request, 'home.html', {'reviews': reviews})

@login_required
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Asigna el usuario logueado
            review.movie = movie        # Asigna la película
            review.save()
            return redirect('movie_catalog')  # Ajusta la redirección según tu aplicación
    else:
        form = ReviewForm()

    return render(request, 'review_form.html', {'form': form, 'movie': movie})