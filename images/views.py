from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage

from .models import TrailImage

# Method to send an email once an image is approved
def send_approval_email(user):
    subject = "HikeIt: Image Approval"
    to = [user.email]
    from_email = 'image-approval@hikeit.me'

    ctx = {
        'user': user
    }

    message = get_template('images/email/approved.html').render(Context(ctx))
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

def index(request):
    images = TrailImage.objects.filter(approved=False)
    return render(request, 'images/index.html', {'images': images})
    
def approve(request, image_id):
    if request.user.is_authenticated and request.user.is_staff:
        image = TrailImage.objects.get(pk=image_id)
        image.approved = True
        image.save()
        send_approval_email(image.user)
        return HttpResponseRedirect('/image/')
