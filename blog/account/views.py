#!coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from forms import UserForm
from models import Users
#from django.core.context_processors import csrf
from django.template import RequestContext

# Create your views here.
def register(request):
	if request.method=='POST':
		#c={}
		#x`c.update(csrf(request))
		uf = UserForm(request.POST)
		if uf.is_valid():
			#判断并获取表单
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			email = uf.cleaned_data['email']
			#入库
			user = Users()
			user.username = username
			user.password = password
			user.email = email
			user.save()
			return render_to_response('success.html',{'username':username},context_instance=RequestContext(request))

	else:
		uf = UserForm()
	return render_to_response('register.html',{'uf':uf},context_instance=RequestContext(request))				
def reg_wait():
	pass
def reg_active():	
	pass