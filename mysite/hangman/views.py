from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Word
import random

def index(request):
    hangman_words = Word.objects.all()
    random_word = random.choice(hangman_words)
    context = {
        'hangman_words' : hangman_words,
        'random_word' : random_word,
        'random_word_array': list(random_word.word_text),
    }
    return render(request, 'hangman/index.html', context)

