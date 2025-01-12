from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10000000, decimal_places=3)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=1000000, decimal_places=3)
    size = models.DecimalField(max_digits=100000, decimal_places=3)
    description = models.TextField()
    age_limited = models.BooleanField(default='False')
    buyer = models.ManyToManyField(Buyer, related_name='games')





