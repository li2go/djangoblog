from django.shortcuts import render_to_response

from djangoblog.models import *
from django import template

# Create your views here.
#from django.views.generic.list import

#view of index
def index(self):
	blogs=Article.objects.all()
	return render_to_response("index.html",{"blogs":blogs})
 

 