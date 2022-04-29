from django.urls import path
from . import views

app_name = 'board_games'
urlpatterns = [
    path('', views.index, name='index'),
    path('gamers/', views.gamers, name='gamers'),
    path('games/', views.games, name='games'),
    path('loans/', views.loans, name='loans'),
    
    path('new_loan/', views.new_loan, name='new_loan'),
    path('new_game/', views.new_game, name='new_game'),
    
    #path('games/<int:gamer_id/', views.game, name='game'),

]