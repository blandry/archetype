from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def map(request):
    template = loader.get_template('map/map.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
