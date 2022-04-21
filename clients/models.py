from django.db import models


# Create your models here.
# name
# work phone
# cell phone
# email
# groups


class Client(models.Model):
    name = models.CharField(max_length=255)
    # workPhone = models.CharField(max_length=999999)
    cellPhone = models.CharField(max_length=999999)
    email = models.CharField(max_length=999999)
    image_url = models.CharField(max_length=999999)
    balance = models.FloatField(max_length=999999,default=0.0)
    applicationId = models.CharField(max_length=999999,default='0')


class Message(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

class Deposit(models.Model):
    depositID = models.CharField(max_length=255)
    applicationId = models.CharField(max_length=255)
    transactionAmount= models.CharField(max_length=255)
    transactionStatus= models.CharField(max_length=255)
    transactionDate = models.CharField(max_length=255)
    datetime =   models.CharField(max_length=255)
    transactionType=   models.CharField(max_length=255)
    currencyCode =  models.CharField(max_length=255)


class Withdrawal(models.Model):
    withdrawalID = models.CharField(max_length=255)
    applicationId = models.CharField(max_length=255)
    transactionAmount= models.CharField(max_length=255)
    transactionStatus= models.CharField(max_length=255)
    transactionDate = models.CharField(max_length=255)
    datetime =   models.CharField(max_length=255)
    transactionType=   models.CharField(max_length=255)
    currencyCode =  models.CharField(max_length=255)

