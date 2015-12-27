from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from datetime import datetime, timedelta
import time

from .models import Planner
from .tasks import notify_email
from trails.models import Trail

def index(request):
    if request.user.is_authenticated():
        return render(request, 'planner/index.html')
    else:
        messages.add_message(request, messages.WARNING, 'You must sign in to use the trail planning tools')
        return HttpResponseRedirect('/')

def planner(request, trail_id):
    if request.user.is_authenticated():
        trail = get_object_or_404(Trail, pk=trail_id)
        return render(request, 'planner/plan.html', {"trail": trail})
    else:
        messages.add_message(request, messages.WARNING, 'You must sign in to use the trail planning tools')
        return HttpResponseRedirect('/')

def plan(request):
    if request.user.is_authenticated():
        date = request.POST["date"]
        hiking_time = datetime.fromtimestamp(time.mktime(time.strptime(date, "%m/%d/%Y")))
        notification_send_date = hiking_time - timedelta(days=1)
        trail = get_object_or_404(Trail, pk=int(request.POST.get("trail_id")))
        planner = Planner.objects.create(trail=trail, hiking_time=hiking_time)
        planner.save()
        notify_email.apply_async(eta=notification_send_date, kwargs={'pk_user': request.user.pk, 'pk_planner': planner.pk})
        messages.add_message(request, messages.SUCCESS, 'Hike scheduled')
        return HttpResponseRedirect('/planner/')
    else:
        messages.add_message(request, messages.WARNING, 'You must sign in to use the trail planning tools')
        return HttpResponseRedirect('/')
