from django.db import models

# Create your models here.


class Historyinfo(models.Model):
    result= models.CharField(max_length=100)
    email = models.EmailField()