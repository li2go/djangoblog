#coding:utf-8
from django.db import models
from django.db.models import F

#from django.views.generic.list import ListView
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title =models.CharField(max_length=150)
    content =models.TextField()
    content=RichTextField('正文')
    timestamp =models.DateTimeField()
    like = models.IntegerField()
    age = models.CharField(max_length=150)

    def add_like(self,article_id):
    	article = self.objects.get(like=article_id)
    	article.like = F('like')+1
    	article.save()


    
