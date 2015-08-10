from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Trail

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
