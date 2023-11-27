from django.db import models
from django.contrib.postgres.fields import ArrayField

class Users(models.Model): 
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)

class Items(models.Model):
    productType = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    materials = 
    images =
    specifier =
    price =
    desc =