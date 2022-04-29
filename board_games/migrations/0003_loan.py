# Generated by Django 4.0.4 on 2022-04-22 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board_games', '0002_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('gamers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board_games.gamer')),
                ('name_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board_games.game')),
            ],
        ),
    ]