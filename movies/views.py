from django.shortcuts import render
from .models import Movie
from django.contrib.auth.decorators import login_required
import logging


@login_required
def movie_catalog(request):
    # Obtén todas las películas de la base de datos
    movies = Movie.objects.all()
    # Pasa las películas al contexto de la plantilla
    return render(request, 'movie_catalog.html', {'movies': movies})

logger = logging.getLogger(__name__)  # Configuración del logger

def movie_list(request):
    movies = Movie.objects.all()

    # Registrar en el log los IDs de las películas
    logger.debug(f"Movies IDs: {[movie.id for movie in movies]}")

    return render(request, 'movies/movie_list.html', {'movies': movies})


