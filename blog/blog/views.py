#!coding:utf-8
from django.shortcuts import render_to_response
from django.core.paginator import Paginator,InvalidPage,EmptyPage

from djangoblog.models import *
#from django import template

# Create your views here.
#from django.views.generic.list import

#view of index
def iindex(request):
	article=Article.objects.all()
	PageSize=1
	blogs=Paginator(article,PageSize) 
	"""
	Paginator类方法说明

	Paginator(models,cut_number) >>> 把MODELS，以CUT_NUMBER为单位进行分割，
    models=6  self=Paginator(models,2) >>> 一共6条数据，以2位单位 ,分得6/2=3 页

    self.num_pages  >>> 返回页数  这里=3

	self.has_next() >>> 是否有下一页 返回布尔值   TRUE OR FALSE
	 
	self.has_previous() >>> 同上，是否有前一页 
	
	self.has_other_pages() >>> 是否有其他页 返回布尔值，这个基本不用
	  
	self.next_page_number() >>> 返回下一页的值   值为INT类型  
	 
	self.previous_page_number() >>> 返回前一页的值  值为INT类型

	"""
	#列表形式返回分数    ex:一共5分5页 self.page_range   return[1,2,3,4,5]
	page_range=blogs.page_range   
	try:
		#self.GET.get(a,b)  获取RUL请求，如果请求中没有a， 把b赋值给a ,REUTRN URL?a=b .
		page = int(request.GET.get('page',1)) 
	except ValueError:
	    page = 1
	    print page
	try:
	    posts=blogs.page(page)
 	except:
 		posts=blogs.page(blogs.num_pages)    	
	return render_to_response("index/home.html",{"blogs":article,"page_div":posts,"page_range":page_range})
 
	
 