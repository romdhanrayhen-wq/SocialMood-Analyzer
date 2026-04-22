from django.db import models

class Analyse(models.Model):
    SENTIMENT_CHOICES = [
        ('Positif', 'Positif'),
        ('Neutre',  'Neutre'),
        ('Negatif', 'Negatif'),
    ]

    texte     = models.TextField()
    sentiment = models.CharField(max_length=20, choices=SENTIMENT_CHOICES)
    score     = models.FloatField()
    date      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.sentiment} ({self.score}) - {self.texte[:50]}"
