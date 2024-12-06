from django.urls import path
from . import views
from reviews.views import add_review

urlpatterns = [
    path('movie_catalog', views.movie_catalog, name='movie_catalog'),  # Ruta para la pantalla de inicio
    path('add_review/<int:movie_id>/', add_review, name='add_review'),
]