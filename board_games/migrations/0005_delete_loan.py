# Generated by Django 4.0.4 on 2022-04-22 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board_games', '0004_alter_loan_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Loan',
        ),
    ]
