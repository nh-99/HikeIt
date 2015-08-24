from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import uuid

def send_confirm_email(user, token):
    subject = "HikeIt: User Account Confirmation"
    to = [user.email]
    from_email = 'user-confirm@hikeit.me'

    ctx = {
        'user': user,
        'token': token
    }

    message = get_template('users/email/confirm.html').render(Context(ctx))
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()
        
def registeruser(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    token = uuid.uuid1().hex
    if not request.user.is_authenticated():
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False
        user.profile.token = token
        user.save()
        send_confirm_email(user, user.profile.token)
        messages.add_message(request, messages.SUCCESS, 'The account was successfully registered. Please check for an activation email.')
        return HttpResponseRedirect('/')
    else:
        messages.add_message(request, messages.WARNING, 'You are already signed in')
        return HttpResponseRedirect('/')
        
def confirmuser(request):
    uid = request.GET['uid']
    token = request.GET['token']
    
    if not request.user.is_authenticated():
        user = get_object_or_404(User, pk=uid)
        user.is_active = True
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Your account has been activated. You may now login')
        return HttpResponseRedirect('/login/')
    else:
        messages.add_message(request, messages.WARNING, 'You are already signed in')
        return HttpResponseRedirect('/')
    
