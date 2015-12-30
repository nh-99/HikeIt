from datetime import datetime
from django import template

register = template.Library()

@register.simple_tag
def format_time_cal(time):
    return time.strftime('%Y-%m-%d')

@register.simple_tag
def format_time_view(time):
    return time.strftime('%A, %B %w at %I:%M %P')
