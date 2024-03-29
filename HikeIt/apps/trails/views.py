from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.conf import settings

from .models import Trail
from .forms import TrailImageForm, TrailReviewForm

from django.template.loader import render_to_string, get_template
from django.template import Context
from django.core.mail import EmailMessage

from images.models import TrailImage
from reviews.models import Review

# Method to send an email once a trail is approved
def send_approval_email(user, approved, trail):
    subject = "HikeIt: Trail Approval"
    to = [user.email]
    from_email = 'trail-approval@hikeit.me'

    ctx = {
        'user': user,
        'trail': trail
    }

    if approved:
        message = get_template('trails/email/approved.html').render(Context(ctx))
    else:
        message = get_template('trails/email/denied.html').render(Context(ctx))
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

def approve_trail_list(request):
    if request.user.is_authenticated() and request.user.is_staff:
        trails = Trail.objects.filter(approved=False)
        return render(request, 'trails/approval_list.html', { 'trails': trails })
    else:
        messages.add_message(request, messages.WARNING, 'You do not have sufficient access to perform this function')
        return HttpResponseRedirect('/')

def approve_trail(request):
    if request.user.is_authenticated() and request.user.is_staff:
        trail_id = request.GET['id']
        trail = Trail.objects.get(pk=trail_id)
        trail.approved = True
        trail.save()
        send_approval_email(trail.submitter, True, trail)
        messages.add_message(request, messages.SUCCESS, 'The trail has been approved successfully')
        return HttpResponseRedirect('/trail/trails/')
    else:
        messages.add_message(request, messages.WARNING, 'You do not have sufficient access to perform this function')
        return HttpResponseRedirect('/')

def new(request):
    return render(request, 'trails/new.html')

def create_trail(request):
    if request.user.is_authenticated():
        name = request.POST['name']
        difficulty = request.POST['diff']
        distance = request.POST['distance']
        latitude = request.POST['lat']
        longitude = request.POST['long']
        location = request.POST['location']
        
        trail = Trail.objects.create(name=name, lat=latitude, long=longitude, difficulty=difficulty, distance=distance, location=location, submitter=request.user)
        trail.save()
        
        messages.add_message(request, messages.SUCCESS, 'The trail has been submitted for review')
        return HttpResponseRedirect('/')
    else:
        messages.add_message(request, messages.WARNING, 'You need to be signed in to submit trails!')
        return HttpResponseRedirect('/')

def trailpage(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    length = str(trail.distance)
    difficulty = str(trail.difficulty)
    
    images = trail.trailimage_set.filter(approved=True)
    reviews = trail.review_set.all
    
    liked = False
    completed = False
    saved = False
    
    if request.user.is_authenticated():
        try:
            liked = request.user.profile.liked_trails.get(pk=trail.pk)
        except trail.DoesNotExist:
            liked = False
            
        try:
            completed = request.user.profile.completed_trails.get(pk=trail.pk)
        except trail.DoesNotExist:
            completed = False
            
        try:
            saved = request.user.profile.saved_trails.get(pk=trail.pk)
        except trail.DoesNotExist:
            saved = False
            
    
    args = {'trail': trail,
            'length': length,
            'difficulty': difficulty,
            'id': trail_id,
            'images': images,
            'reviews': reviews,
            'liked': liked,
            'completed': completed,
            'saved': saved
           }
    
    return render(request, 'trails/trailpage.html', args)
    
def traillocation(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    paths = trail.path_set.all()
    
    args = {'trail': trail,
            'id': trail_id,
            'paths': paths,
            'domain': settings.HOSTNAME
           }
    
    return render(request, 'trails/trail_location.html', args)

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
    
def unliketrail(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    user = request.user
    
    if request.user.is_authenticated():
        try:
            user.profile.liked_trails.get(pk=trail_id)
        except trail.DoesNotExist:
            messages.add_message(request, messages.WARNING, 'You have not liked this trail yet')
            return HttpResponseRedirect('/trail/%s' % str(trail_id))
        else:
            # Add the trail to the user model, in a many to many state
            user.profile.liked_trails.remove(trail)
            user.save()
            
            trail.likes = trail.likes - 1
            trail.save()
    else:
        messages.add_message(request, messages.WARNING, 'You need to be signed in to un-like trails!')
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
    
def uncompletetrail(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    user = request.user
    
    if request.user.is_authenticated():
        try:
            user.profile.completed_trails.get(pk=trail_id)
        except trail.DoesNotExist:
            messages.add_message(request, messages.WARNING, 'You have not yet marked this trail as completed')
            return HttpResponseRedirect('/trail/%s' % str(trail_id))
        else:
            # Add the trail to the user model, in a many to many state
            user.profile.completed_trails.remove(trail)
            user.save()
            
    else:
        messages.add_message(request, messages.WARNING, 'You need to be signed in to unmark trails as completed!')
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
        if request.user.is_authenticated():
            if form.is_valid():
                image = TrailImage()
                image.image = form.cleaned_data['image']
                image.user = request.user
                image.trail = get_object_or_404(Trail, pk=trail_id)
                image.save()
                messages.add_message(request, messages.SUCCESS, 'Image uploaded successfully!')
                return HttpResponseRedirect('/trail/%s' % str(trail_id))
                
    return render(request, 'trails/trail_image_form.html', {'trail_id':trail_id, 'form':form})
    
def create_review(request, trail_id):
    if request.method == 'POST':
        if request.user.is_authenticated():
            if request.POST.get('review_text') != '':
                review = Review()
                review.review_text = request.POST.get('review_text')
                review.user = request.user
                review.trail = get_object_or_404(Trail, pk=trail_id)
                review.save()
                return HttpResponseRedirect('/trail/%s' % str(trail_id))
            else:
                messages.add_message(request, messages.WARNING, 'No comment text was provided')
                return HttpResponseRedirect('/trail/%s/' % str(trail_id))
                
    return render(request, 'trails/create_review.html', {'trail_id':trail_id, 'form':form})
    
def savedtrail(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    user = request.user
    
    if request.user.is_authenticated():
        try:
            user.profile.saved_trails.get(pk=trail_id)
        except trail.DoesNotExist:
            # Add the trail to the user model, in a many to many state
            user.profile.saved_trails.add(trail)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'You have saved the trail ' + trail.name)
            
    else:
        messages.add_message(request, messages.WARNING, 'You need to be signed in to save trails!')
        return HttpResponseRedirect('/trail/%s' % str(trail_id))
        
    try:
        return HttpResponseRedirect('/trail/%s' % str(trail_id))
    except:
        pass
    return HttpResponse("Completed")
    
def unsavetrail(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    user = request.user
    
    if request.user.is_authenticated():
        try:
            user.profile.saved_trails.get(pk=trail_id)
        except trail.DoesNotExist:
            messages.add_message(request, messages.WARNING, 'You have not yet saved this trail')
            return HttpResponseRedirect('/trail/%s' % str(trail_id))
        else:
            # Add the trail to the user model, in a many to many state
            user.profile.saved_trails.remove(trail)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'You have un-saved the trail ' + trail.name)
            
    else:
        messages.add_message(request, messages.WARNING, 'You need to be signed in to save trails!')
        return HttpResponseRedirect('/trail/%s' % str(trail_id))
        
    try:
        return HttpResponseRedirect('/trail/%s' % str(trail_id))
    except:
        pass
    return HttpResponse("Completed")
