from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.contrib import messages

from .models import Review

# Method to send an email once an review is approved
def send_approval_email(user):
    subject = "HikeIt: Review Approval"
    to = [user.email]
    from_email = 'review-approval@hikeit.me'

    ctx = {
        'user': user
    }

    message = get_template('reviews/email/approved.html').render(Context(ctx))
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

def index(request):
    if request.user.is_authenticated() and request.user.is_staff:
        reviews = Review.objects.filter(approved=False)
        return render(request, 'reviews/index.html', {'reviews': reviews})
    else:
        messages.add_message(request, messages.WARNING, 'You do not have significant access to perform this function')
        return HttpResponseRedirect('/login/')
    
def approve(request, review_id):
    if request.user.is_authenticated and request.user.is_staff:
        review = Review.objects.get(pk=review_id)
        review.approved = True
        review.save()
        send_approval_email(review.user)
        messages.add_message(request, messages.SUCCESS, 'Review has been approved successfully')
        return HttpResponseRedirect('/reviews/')
    else:
        messages.add_message(request, messages.WARNING, 'You do not have significant access to perform this function')
        return HttpResponseRedirect('/login/')
