from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db import IntegrityError

from .models import Issue
from trails.models import Trail

def send_submission_email(user):
    subject = "HikeIt: Trail Fixes"
    to = [user.email]
    from_email = 'trail-accuracy@hikeit.me'

    ctx = {
        'user': user
    }

    message = get_template('issues/email/submitted.html').render(Context(ctx))
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

def create_issue(request, trail_id):
    if request.user.is_authenticated():
	troublesome_trail = get_object_or_404(Trail, pk=trail_id)
        if request.method == "POST":
            issue = Issue()
            issue.user = request.user
            issue.issue_text = request.POST.get('issue_text')
            issue.trail = troublesome_trail
            try:
		issue.save()
	    except IntegrityError:
		messages.add_message(request, messages.WARNING, 'Please fill out the form correctly!')
	        return HttpResponseRedirect('/issues/{0}/'.format(trail_id))
            messages.add_message(request, messages.SUCCESS, 'Trail issue submitted successfully!')
            send_submission_email(request.user)
            return HttpResponseRedirect('/trails/{0}/'.format(trail_id))
        return render(request, 'issues/submit.html', { 'trail_id': trail_id, 'trail': troublesome_trail })
    else:
        messages.add_message(request, messages.WARNING, 'You need to be signed in to fix trails!')
        return HttpResponseRedirect('/login/')
