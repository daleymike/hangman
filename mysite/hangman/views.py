from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Word

def index(request):
    hangman_words = Word.objects.all()
    context = {
        'hangman_words' : hangman_words
    }
    return render(request, 'hangman/index.html', context)

