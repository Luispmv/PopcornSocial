from django.urls import path
from account.views import user_login, register_view
from home.views import home

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', register_view, name='register'),
    path('home/', home, name='home'),
]