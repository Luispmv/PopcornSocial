from django.contrib import admin
from .models import Movie, Genre

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre')  # Mostrar género en la lista
    search_fields = ('title',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)