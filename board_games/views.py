from django.shortcuts import get_object_or_404, redirect, render

import board_games
from .models import Gamer, Game, Loan
from .forms import LoanForm, GameForm

# Create your views here.
def index(request):
    return render(request, 'board_games/index.html')

def gamers(request):
    gamers = Gamer.objects.order_by('date_added')
    context = {'gamers': gamers}
    return render(request, 'board_games/gamers.html', context)

def games(request):
    games = Game.objects.order_by('date_added')
    
    context = {'games': games}
    return render(request, 'board_games/games.html', context)

def loans(request):
    loans = Loan.objects.order_by('date_added')
    
    context = {'loans': loans}
    return render(request, 'board_games/loans.html', context)


def new_loan(request):
    if request.method != 'POST':
        form = LoanForm()
    else:
        form = LoanForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_games:loans')
    context = {'form':form}
    return render(request, 'board_games/new_loan.html', context)

def new_game(request):
    if request.method != 'POST':
        form = GameForm()
    else:
        form = GameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_games:games')
    context = {'form':form}
    return render(request, 'board_games/new_game.html', context)




