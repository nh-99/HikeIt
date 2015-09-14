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
    
def profile(request):
    if request.user.is_authenticated():
        return render(request, 'users/profile.html')
    else:
        messages.add_message(request, messages.WARNING, 'You need to be signed in to see your profile')
        return HttpResponseRedirect('/')
        
def profile_settings(request):
    if request.user.is_authenticated():
        return render(request, 'users/profile_settings.html')
    else:
        messages.add_message(request, messages.WARNING, 'You need to be signed in to see your profile')
        return HttpResponseRedirect('/')
        
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
    
    
def do_update(user, **kwargs):
	for name, field in kwargs.items():
		if field != '':
			if name != 'password':
				exec("global user; user.{0} = '{1}'".format(name, field), {'user':user})
			else:
				exec("global user; user.set_password('{0}')".format(field), {'user':user})
	user.save()
			
def update_profile(request):
	user = request.user
	new_email = request.POST.get('email', default=user.email)
	new_password = request.POST.get('password')
	new_first_name = request.POST.get('firstname', default=user.first_name)
	new_last_name = request.POST.get('lastname', default=user.last_name)
	
	if user.is_authenticated():
		do_update(user, email = new_email, password = new_password, first_name = new_first_name, last_name = new_last_name)
		messages.add_message(request, messages.SUCCESS, 'Profile updated successfully')
		return HttpResponseRedirect('/user/profile/')
	else:
		messages.add_message(request, messages.SUCCESS, 'You need to be logged in to update your profile!')
		return HttpResponseRedirect('/login/')
