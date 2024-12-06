from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']  # Solo se incluyen estos campos, ya que `user` y `movie` se asignan en la vista
        widgets = {
            'review_text': forms.Textarea(attrs={
                'class': 'w-full p-3 rounded-lg bg-gray-700 text-white focus:ring-2 focus:ring-yellow-400',
                'placeholder': 'Escribe tu reseña aquí...',
                'rows': 5,
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'w-full p-3 rounded-lg bg-gray-700 text-white focus:ring-2 focus:ring-yellow-400',
                'min': 1,
                'max': 5,
                'placeholder': 'Calificación (1-5)',
            }),
        }
        labels = {
            'review_text': 'Tu reseña',
            'rating': 'Calificación',
        }
        help_texts = {
            'rating': 'Por favor, selecciona una calificación entre 1 y 5.',
        }
