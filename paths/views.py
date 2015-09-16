from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Path
from .forms import PathForm

from trails.models import Trail

def upload_trail_path(request, trail_id):
    form = PathForm()
    if request.method == 'POST':
        form = PathForm(request.POST, request.FILES)
        if request.user.is_authenticated():
            if form.is_valid():
                path = Path(path_file=request.FILES['path_file'])
                path.user = request.user
                path.trail = get_object_or_404(Trail, pk=trail_id)
                path.save()
                messages.add_message(request, messages.SUCCESS, 'Path uploaded successfully!')
                return HttpResponseRedirect('/trail/%s' % str(trail_id))
                
    return render(request, 'paths/path_upload.html', {'trail_id':trail_id, 'form':form})
