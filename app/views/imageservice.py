from django import http
from django import template
from django.contrib import messages
from django.shortcuts import redirect, render_to_response

def index(request):

    return render_to_response('django_nova/instances/index.html', {
        
    }, context_instance = template.RequestContext(request))
