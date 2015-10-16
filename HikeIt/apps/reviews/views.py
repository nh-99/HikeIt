from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Review

def delete_review(request, review_id):
	if request.user.is_authenticated and request.user.is_staff:
		review = Review.objects.get(pk=review_id)
		review.delete()
		messages.add_message(request, messages.SUCCESS, 'Comment deleted successfully')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
