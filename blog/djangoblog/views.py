#!coding:utf-8
from django.shortcuts import render_to_response
from django.core.paginator import Paginator,InvalidPage,EmptyPage

from djangoblog.models import *
from django import template

# Create your views here.
#from django.views.generic.list import

#view of index
def index(request):
	article=Article.objects.all()
	PageSize=1
	blogs=Paginator(article,PageSize) 
	page_range=blogs.page_range  #列表形式返回分数    ex:一共5分5页 self.page_range   return[1,2,3,4,5] 
	try:
		page = int(request.GET.get('page',1))
	except ValueError:
	    page = 1
	    print page
	try:
	    posts=blogs.page(page)
 	except:
 		posts=blogs.page(blogs.num_pages)    	
	return render_to_response("index.html",{"blogs":article,"page_div":posts,"page_range":page_range})
 

 