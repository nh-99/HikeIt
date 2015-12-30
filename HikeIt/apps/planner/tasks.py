from celery.decorators import task

from pypebbleapi import Timeline

from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage

from django.contrib.auth.models import User
from .models import Planner

from datetime import datetime

# Handles the notification's sent to users for schedules hikes

@task
def notify_email(pk_user, pk_planner):
    user = User.objects.get(pk=pk_user)
    planner = Planner.objects.get(pk=pk_planner)
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

@task
def notify_pebble(pk_user, pk_planner):
    user = User.objects.get(pk=pk_user)
    token = user.profile.timeline_token
    planner = Planner.objects.get(pk=pk_planner)
    
    # send pin
    timeline = Timeline()

    my_pin = dict(
        id='hikeit-' + str(planner.pk),
        time=planner.hiking_time.isoformat(),
        layout=dict(
            type="genericPin",
            title="This is a genericPin!",
            tinyIcon="system://images/NOTIFICATION_REMINDER",
        )
    )

    timeline.send_user_pin(
        user_token=token,
        pin=my_pin,
    )

