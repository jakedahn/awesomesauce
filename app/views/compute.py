from django import http
from django import template
from django.contrib import messages
from django.shortcuts import redirect, render_to_response

def index(request):

    return render_to_response('compute/index.html', {
    }, context_instance = template.RequestContext(request))

def instances(request):

    return render_to_response('compute/instances.html', {
    }, context_instance = template.RequestContext(request))


def volumes(request):

    return render_to_response('compute/volumes.html', {
    }, context_instance = template.RequestContext(request))

def security(request):

    return render_to_response('compute/security.html', {
    }, context_instance = template.RequestContext(request))

def vpn(request):

    return render_to_response('compute/vpn.html', {
    }, context_instance = template.RequestContext(request))


