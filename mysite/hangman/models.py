from django.db import models

class Word(models.Model):
    word_text = models.CharField(max_length=10)
    letter_count = models.IntegerField(default=0)

    def __str__(self):
        return self.word_text
