from django.shortcuts import render

from trails.models import Trail

def location(request, location):
	trails = Trail.objects.filter(location__contains=location)[:50]
	
	args = {'trails': trails, 'location': location}
	
	return render(request, 'search/results.html', args)
	
def name(request, name):
	trails = Trail.objects.filter(name__contains=name)[:50]
	
	args = {'trails': trails, 'location': name}
	
	return render(request, 'search/results.html', args)
