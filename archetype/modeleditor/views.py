from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def new(request):
    template = loader.get_template('modeleditor/new.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
