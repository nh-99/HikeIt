from django.shortcuts import render

from .models import Planner

def index(request):
    if request.user.is_authenticated():
        try:
            planner = Planner.objects.get(user=request.user)
        except Planner.DoesNotExist:
            planner = None
        return render(request, 'planner/index.html', { "planner": planner })
    else:
        messages.add_message(request, messages.WARNING, 'You must sign in to use the trail planning tools')
        return HttpResponseRedirect('/')
