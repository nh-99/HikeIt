from django.shortcuts import render

from trails.models import Trail

def location(request, location):
	request.session['searchtype'] = 'location'
	
	trails = Trail.objects.filter(location__contains=location)[:50]
	
	args = {'trails': trails, 'location': location, 'searchtype': request.session['searchtype']}
	
	return render(request, 'search/results.html', args)
	
def name(request, name):
	request.session['searchtype'] = 'name'
	
	trails = Trail.objects.filter(name__contains=name)[:50]
	
	args = {'trails': trails, 'location': name, 'searchtype': request.session['searchtype']}
	
	return render(request, 'search/results.html', args)
