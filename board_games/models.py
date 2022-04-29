from tabnanny import verbose
from django.db import models
from django.utils import timezone


# Create your models here.
class Gamer(models.Model):
    name = models.CharField(max_length=50)
    
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    name_game = models.CharField(max_length=200)
   
    
    date_added = models.DateTimeField(auto_now_add=True)

    
    
    def __str__(self):
        return self.name_game

class Loan(models.Model):
    #name = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    #game = models.ForeignKey(Game, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, default='')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'loans'

    def __str__(self):
        return f' {self.text[:100]} .'



