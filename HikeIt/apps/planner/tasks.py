from celery.decorators import task

from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage

from django.contrib.auth.models import User

# Handles the notification's sent to users for schedules hikes

@task
def notify_email(pk_user, pk_planner):
    user = User.objects.get(pk=pk_user)
    planner = user.profile.planned_hikes.get(pk=pk_planner)
    subject = "HikeIt: Hiking Reminder!"
    to = [user.email]
    from_email = 'reminder@hikeit.me'

    ctx = {
        'user': user,
        'planner': planner
    }
    
    message = get_template('planner/email/reminder.html').render(Context(ctx))
    
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()
