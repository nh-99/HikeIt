from django import template

register = template.Library()

@register.simple_tag
def reset_facebook_var(request):
    request.session['redirect_pebble'] = False
    return ''
