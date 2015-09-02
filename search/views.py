from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from trails.models import Trail

def location(request, location):
	request.session['searchtype'] = 'location'
	
	trail_list = Trail.objects.filter(location__contains=location, approved=True)[:50]
        paginator = Paginator(trail_list, 10)
        
        total = trail_list.count()
        
        page = request.GET.get('page')
        try:
            trails = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            trails = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            trails = paginator.page(paginator.num_pages)
	
	args = {'trails': trails, 'location': location, 'total': total}
	
	return render(request, 'search/results.html', args)
	
def name(request, name):
	request.session['searchtype'] = 'name'
	
	trail_list = Trail.objects.filter(name__contains=name, approved=True)[:50]
        paginator = Paginator(trail_list, 10)
        
        total = trail_list.count()
        
        page = request.GET.get('page')
        try:
            trails = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            trails = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            trails = paginator.page(paginator.num_pages)
	
	args = {'trails': trails, 'location': name, 'total': total}
	
	return render(request, 'search/results.html', args)
