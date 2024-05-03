# from django.db import models
from djongo import models
# Create your models here.

class Seed(models.Model):
    _id = models.ObjectIdField()
    rep_date = models.DateField()