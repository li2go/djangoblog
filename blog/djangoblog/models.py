#coding:utf-8
from django.db import models
#from django.views.generic.list import ListView
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title =models.CharField(max_length=150)
    content =models.TextField()
    content=RichTextField('正文')
    timestamp =models.DateTimeField()

