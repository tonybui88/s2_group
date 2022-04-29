from django.contrib import admin

# Register your models here.
from .models import Game, Gamer, Loan
admin.site.register(Gamer)
admin.site.register(Game)
admin.site.register(Loan)
