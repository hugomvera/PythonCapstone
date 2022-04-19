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

class Message(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

