from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Trail
from .forms import TrailImageForm

from images.models import TrailImage

def trailpage(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    length = str(trail.distance)
    difficulty = str(trail.difficulty)
    
    args = {'trail': trail,
            'length': length,
            'difficulty': difficulty,
            'id': trail_id
           }
    
    return render(request, 'trails/trailpage.html', args)

def liketrail(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    
    if request.user.is_authenticated():
        trail.likes = trail.likes + 1
        trail.save()
    #else:
        # TODO: message to user saying to login
    try:
        return HttpResponseRedirect('/trail/%s' % str(trail_id))
    except:
        pass
    return HttpResponse("Like")
    
def upload_trail_image(request, trail_id):
    form = TrailImageForm()
    if request.method == 'POST':
        form = TrailImageForm(request.POST, request.FILES)
        if request.user:
            if form.is_valid():
                image = TrailImage()
                image.image = form.cleaned_data['image']
                image.user = request.user
                image.trail = get_object_or_404(Trail, pk=trail_id)
                image.save()
                messages.add_message(request, messages.SUCCESS, 'Image uploaded successfully!')
                return HttpResponseRedirect('/trail/%s' % str(trail_id))
                
    return render(request, 'trails/trail_image_form.html', {'trail_id':trail_id, 'form':form})
