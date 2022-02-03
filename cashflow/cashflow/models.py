from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    balance = models.IntegerField()


class Influence(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    bills = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bills'
    )
    balance_history = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='balance_history'
    )
    date = models.DateField()
