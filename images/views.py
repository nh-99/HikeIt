from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import TrailImage

def index(request):
    images = TrailImage.objects.filter(approved=False)
    return render(request, 'images/index.html', {'images': images})
    
def approve(request, image_id):
    if request.user.is_authenticated and request.user.is_staff:
        image = TrailImage.objects.get(pk=image_id)
        image.approved = True
        image.save()
        return HttpResponseRedirect('/image/')
