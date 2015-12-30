from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from datetime import datetime, timedelta
import time

from .models import Planner
from .tasks import notify_email, notify_pebble
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
        date = request.POST.get("date") + ' ' + request.POST.get("time")
        print date
        if request.POST["delay"] != '':
            notification_delay = request.POST["delay"]
        else:
            notification_delay = 1
        hiking_time = datetime.fromtimestamp(time.mktime(time.strptime(date, "%m/%d/%Y %I:%M%p")))
        notification_send_date = hiking_time - timedelta(days=notification_delay)
        trail = get_object_or_404(Trail, pk=int(request.POST.get("trail_id")))
        planner = Planner.objects.create(trail=trail, hiking_time=hiking_time, notification_date=notification_send_date)
        request.user.profile.planned_hikes.add(planner)
        request.user.save()
        notify_email.apply_async(eta=notification_send_date, kwargs={'pk_user': request.user.pk, 'pk_planner': planner.pk})
        if request.user.profile.timeline_token is not None:
            notify_pebble.apply_async(eta=hiking_time - timedelta(days=1), kwargs={'pk_user': request.user.pk, 'pk_planner': planner.pk})
        messages.add_message(request, messages.SUCCESS, 'Hike scheduled')
        return HttpResponseRedirect('/planner/')
    else:
        messages.add_message(request, messages.WARNING, 'You must sign in to use the trail planning tools')
        return HttpResponseRedirect('/')
        
def view_plan(request, planner_id):
    planner = get_object_or_404(Planner, pk=planner_id)
    # If user is authenticated and the planner is in their list of planners continue
    if request.user.is_authenticated() and request.user.profile.planned_hikes.get(pk=planner.pk):
        return render(request, 'planner/view.html', {'planner': planner})
    else:
        messages.add_message(request, messages.WARNING, 'You must sign in to use the trail planning tools')
        return HttpResponseRedirect('/')
        
def delete_plan(request, planner_id):
    if request.user.is_authenticated():
        Planner.objects.get(pk=planner_id).delete()
        messages.add_message(request, messages.SUCCESS, 'Hike plan deleted successfully')
        return HttpResponseRedirect('/planner/')
    else:
        messages.add_message(request, messages.WARNING, 'You must sign in to use the trail planning tools')
        return HttpResponseRedirect('/')
