from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def new(request):
    template = loader.get_template('modeleditor/new.html')
    context = RequestContext(request, {
            "datasets": [{"name": "Fire unit responses", 
                          "icon": "fire",
                          },
                         {"name": "Tree canopy",
                          "icon": "tree-deciduous",
                          },
                         {"name": "Employment rates", 
                          "icon": "stats",
                          },
                         {"name": "Police officer presence", 
                          "icon": "star",
                          },
                         {"name": "Unsolved murders",
                          "icon": "screenshot",
                          },
                         ],
            })
    return HttpResponse(template.render(context))
