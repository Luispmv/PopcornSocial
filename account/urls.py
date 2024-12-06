from django.urls import path
from movies import views

urlpatterns = [
    path('movie_catalog/', views.movie_catalog, name='movie_catalog'),  # Ruta para la pantalla de inicio
]