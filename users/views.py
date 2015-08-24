from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
        
def registeruser(request):
    username = request.POST['username']
    password = request.POST['password']

def logout_user(request):
    if request.user.is_authenticated():
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'You have been logged out successfully')
        return HttpResponseRedirect('/')
    else:
        messages.add_message(request, messages.WARNING, 'You are not signed in')
        return HttpResponseRedirect('/user/login/')
