from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def index(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))

def about(request):
    return render_to_response('home/about.html', context_instance=RequestContext(request))