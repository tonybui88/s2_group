from django import forms
from .models import Loan, Game

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
       
        fields = ['text']
        lables = {'text':''}

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name_game']
        lables = {'name_game':''}
