from django.contrib import admin
from .models import Review

# Registra el modelo Review en el admin de Django
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating', 'created_at')
    search_fields = ('user__username', 'movie__title')
    list_filter = ('created_at', 'rating')