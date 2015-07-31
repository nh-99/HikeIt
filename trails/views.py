from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Trail

def trailpage(request, trail_id):
	trail = get_object_or_404(Trail, pk=trail_id)
	length = str(trail.distance)
	difficulty = str(trail.difficulty)
	
	args = {'trail': trail,
	        'length': length,
	        'difficulty': difficulty
	       }
	
	return render(request, 'trails/trailpage.html', args)
