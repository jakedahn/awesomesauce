from django import http
from django import template
from django.contrib import messages
from django.shortcuts import redirect, render_to_response
import api

def index(request):
    compute_api = api.get_compute_api()
    flavors = compute_api.flavors.list()

    return render_to_response('dashboard/index.html', {
        
    }, context_instance = template.RequestContext(request))


def treemap(request):
    return render_to_response('dashboard/treemap.html', {
        
    }, context_instance = template.RequestContext(request))
    
