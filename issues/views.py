from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

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
		if request.method == "POST":
			issue = Issue()
			issue.user = request.user
			issue.trail = get_object_or_404(Trail, pk=trail_id)
			issue.issue_text = request.POST.get('issue_text')
			issue.save()
			messages.add_message(request, messages.SUCCESS, 'Trail issue submitted successfully!')
			send_submission_email()
			return HttpResponseRedirect('/trails/{0}/'.format(trail_id))
		return render(request, 'issues/submit.html')
	else:
		messages.add_message(request, messages.WARNING, 'You need to be signed in to fix trails!')
		return HttpResponseRedirect('/login/')
