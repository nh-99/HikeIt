from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Trail
from .forms import TrailImageForm, TrailReviewForm

from images.models import TrailImage
from reviews.models import Review

def trailpage(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    length = str(trail.distance)
    difficulty = str(trail.difficulty)
    
    args = {'trail': trail,
            'length': length,
            'difficulty': difficulty,
            'id': trail_id,
            'searchtype': request.session['searchtype']
           }
    
    return render(request, 'trails/trailpage.html', args)

def liketrail(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    user = request.user
    
    if request.user.is_authenticated():
        try:
            user.profile.liked_trails.get(pk=trail_id)
        except trail.DoesNotExist:
            # Add the trail to the user model, in a many to many state
            user.profile.liked_trails.add(trail)
            user.save()
            
            trail.likes = trail.likes + 1
            trail.save()
    else:
        messages.add_message(request, messages.WARNING, 'You need to be signed in to like trails!')
        return HttpResponseRedirect('/trail/%s' % str(trail_id))
        
    try:
        return HttpResponseRedirect('/trail/%s' % str(trail_id))
    except:
        pass
    return HttpResponse("Like")
    
def completedtrail(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    user = request.user
    
    if request.user.is_authenticated():
        try:
            user.profile.completed_trails.get(pk=trail_id)
        except trail.DoesNotExist:
            # Add the trail to the user model, in a many to many state
            user.profile.completed_trails.add(trail)
            user.save()
            
    else:
        messages.add_message(request, messages.WARNING, 'You need to be signed in to mark trails as completed!')
        return HttpResponseRedirect('/trail/%s' % str(trail_id))
        
    try:
        return HttpResponseRedirect('/trail/%s' % str(trail_id))
    except:
        pass
    return HttpResponse("Completed")
    
def upload_trail_image(request, trail_id):
    form = TrailImageForm()
    if request.method == 'POST':
        form = TrailImageForm(request.POST, request.FILES)
        if request.user:
            if form.is_valid():
                image = TrailImage()
                image.image = form.cleaned_data['image']
                image.user = request.user
                image.trail = get_object_or_404(Trail, pk=trail_id)
                image.save()
                messages.add_message(request, messages.SUCCESS, 'Image uploaded successfully!')
                return HttpResponseRedirect('/trail/%s' % str(trail_id))
                
    return render(request, 'trails/trail_image_form.html', {'trail_id':trail_id, 'form':form, 'searchtype': request.session['searchtype']})
    
def create_review(request, trail_id):
    form = TrailReviewForm()
    if request.method == 'POST':
        form = TrailReviewForm(request.POST)
        if request.user:
            if form.is_valid():
                review = Review()
                review.review_text = form.cleaned_data['review_text']
                review.user = request.user
                review.trail = get_object_or_404(Trail, pk=trail_id)
                review.save()
                messages.add_message(request, messages.SUCCESS, 'Review added successfully')
                return HttpResponseRedirect('/trail/%s' % str(trail_id))
                
    return render(request, 'trails/create_review.html', {'trail_id':trail_id, 'form':form, 'searchtype': request.session['searchtype']})
