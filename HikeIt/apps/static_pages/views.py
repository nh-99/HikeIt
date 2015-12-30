from django.shortcuts import render

def index(request):
    return render(request, 'static_pages/index.html')

def tos(request):
    return render(request, 'static_pages/tos.html')
    
def privacy(request):
    return render(request, 'static_pages/privacy.html')

def pebble_config(request):
    return render(request, 'static_pages/pebble-config.html')
