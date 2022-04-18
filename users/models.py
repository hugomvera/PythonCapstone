from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=255)
    piece = models.CharField(max_length=30)
    balance = models.IntegerField()
