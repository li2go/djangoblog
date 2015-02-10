from django.db import models
#from django.views.generic.list import ListView


# Create your models here.
class Article(models.Model):
    title =models.CharField(max_length=150)
    content =models.TextField()
    timestamp =models.DateTimeField()

