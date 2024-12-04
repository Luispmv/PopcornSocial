from django.urls import path
from account.views import user_login, register_view
from . import views

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', register_view, name='register'),
    path('', views.home, name='home'),  # Ruta para la pantalla de inicio
]