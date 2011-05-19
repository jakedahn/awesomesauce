from django import http
from django import template
from django.contrib import messages
from django.shortcuts import redirect, render_to_response

def index(request):

    return render_to_response('objectstore/index.html', {
    }, context_instance = template.RequestContext(request))

def accounts(request):

    return render_to_response('objectstore/accounts.html', {
    }, context_instance = template.RequestContext(request))

def rings(request):

    return render_to_response('objectstore/rings.html', {
    }, context_instance = template.RequestContext(request))
