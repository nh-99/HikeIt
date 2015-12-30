from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'static_pages/index.html')

def tos(request):
    return render(request, 'static_pages/tos.html')
    
def privacy(request):
    return render(request, 'static_pages/privacy.html')

def pebble_config(request):
    try:
        if request.session.get('redirect_pebble'):
            request.session['redirect_pebble'] = False
        return render(request, 'static_pages/pebble-config.html')
    except AttributeError:
        return render(request, 'static_pages/pebble-config.html')

def pebble_facebook_login(request):
    request.session['redirect_pebble'] = True
    return HttpResponseRedirect('/login/facebook/')
