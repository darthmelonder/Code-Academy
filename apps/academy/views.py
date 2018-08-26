from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from django.urls import reverse
from . import models
# Create your views here.
def index (request,error_message=None):
	return render (request,"academy/index.html",{"error_message": error_message})

def profile (request):
	try:
		u=User.objects.get(user_name=request.POST['user_name'])
		if (u.password==request.POST['password']):
			return render (request,"academy/profile.html",{'user': u})
	except (KeyError, User.DoesNotExist):
		return HttpResponseRedirect (reverse('index',kwargs={'error_message':"Invalid UserName"}))
	return HttpResponseRedirect (reverse('index',kwargs={'error_message':"Wrong Username-Password Combination"}))

def register (request,error_message=None):
	return render (request,"academy/register.html",{'error_message': error_message})

def verify (request):
	try:
		if (request.POST['password']!=request.POST['confirm_password']):
			return HttpResponseRedirect (reverse("register", kwargs={'error_message': "Passwords don't match"}))
		x = User.objects.filter(user_name=request.POST['user_name']).count()
		y = User.objects.filter(mysingle=request.POST['mysingle']).count()
		if (x!=0 or y!=0):
			return HttpResponseRedirect(reverse("register",kwargs={'error_message': "Username or Mysingle already exists"}))
		else:
			user_name = request.POST['user_name']
			password = request.POST['password']
			mysingle = request.POST['mysingle']
			name = request.POST['name']
			u = User (user_name=user_name,password=password, mysingle=mysingle,name=name)
			u.save()
			return HttpResponseRedirect (reverse("index",kwargs={'error_message': "Registered Successfully"}))
	except (KeyError, User.DoesNotExist):
			return HttpResponseRedirect (reverse("register",kwargs={'error_message': "Unknown Error"}))

def problems (request):
	problem_list = models.Problems_List.objects.all()
	return render(request,"academy/problems.html",{'problem_list': problem_list})

def submit (request):
	return HttpResponse("Submit Page!!")

def question (request,problem_id):
	return HttpResponse("Question Page!!")