from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.contrib import messages

from .models import TrailImage

# Method to send an email once an image is approved
def send_approval_email(user, approved, image):
    subject = "HikeIt: Image Approval"
    to = [user.email]
    from_email = 'image-approval@hikeit.me'

    ctx = {
        'user': user,
        'image': image
    }

    if approved:
        message = get_template('images/email/approved.html').render(Context(ctx))
    else:
        message = get_template('images/email/denied.html').render(Context(ctx))
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

def index(request):
    if request.user.is_authenticated() and request.user.is_staff:
        images = TrailImage.objects.filter(approved=False)
        return render(request, 'images/index.html', {'images': images})
    else:
        messages.add_message(request, messages.WARNING, 'You do not have significant access to perform this function')
        return HttpResponseRedirect('/login/')
    
def approve(request, image_id):
    if request.user.is_authenticated and request.user.is_staff:
        image = TrailImage.objects.get(pk=image_id)
        image.approved = True
        image.save()
        send_approval_email(image.user, True, image)
        messages.add_message(request, messages.SUCCESS, 'Image has been approved successfully')
        return HttpResponseRedirect('/image/')
    else:
        messages.add_message(request, messages.WARNING, 'You do not have significant access to perform this function')
        return HttpResponseRedirect('/login/')

def destroy(request, image_id):
    if request.user.is_authenticated and request.user.is_staff:
        image = TrailImage.objects.get(pk=image_id)
        image.delete()
        send_approval_email(image.user, False, image)
        messages.add_message(request, messages.SUCCESS, 'Image has been destroyed successfully')
        return HttpResponseRedirect('/image/')
    else:
        messages.add_message(request, messages.WARNING, 'You do not have significant access to perform this function')
        return HttpResponseRedirect('/login/')
