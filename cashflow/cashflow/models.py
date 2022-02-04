from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    balance = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Influence(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    bills = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bills', null=True, default=None, blank=True
    )
    transactions = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='transactions', null=True, default=None, blank=True
    )
    date = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
