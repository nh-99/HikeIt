from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib import messages

def loggedin(sender, user, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, 'You have been logged in successfully')
    
def loggedout(sender, user, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, 'You have been logged out successfully')

user_logged_in.connect(loggedin)
user_logged_out.connect(loggedout)
