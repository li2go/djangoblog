#!coding:utf-8
from django.shortcuts import render_to_response,render,get_object_or_404
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.views import generic
from djangoblog.models import *
#from django import template

# Create your views here.
#from django.views.generic.list import

#view of index
def index(request):
	article=Article.objects.all()
	PageSize=1
	blogs=Paginator(article,PageSize) 
	#列表形式返回分数    ex:一共5分5页 self.page_range   return[1,2,3,4,5]
	page_range=blogs.page_range   
	try:
		#self.GET.get(a,b)  获取RUL请求，如果请求中没有a， 把b赋值给a ,REUTRN URL?a=b
		page = int(request.GET.get('page',1))  
	except ValueError:
	    page = 1
	    print page
	try:
	    posts=blogs.page(page)
 	except:
 		posts=blogs.page(blogs.num_pages)    	
	return render_to_response("temp/index.html",{"blogs":article,"page_div":posts,"page_range":page_range})
			

class DetailView(generic.DetailView):
	model = Article
	template= 'djangoblog/detail.html'






 