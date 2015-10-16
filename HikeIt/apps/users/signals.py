from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib import messages
from password_reset.signals import user_recovers_password

def loggedin(sender, user, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, 'You have been logged in successfully')
    
def loggedout(sender, user, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, 'You have been logged out successfully')
    
def recover(sender, user, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, 'Password reset successful. Please sign in')

user_logged_in.connect(loggedin)
user_logged_out.connect(loggedout)
user_recovers_password.connect(recover)
