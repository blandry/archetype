from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def new(request):
    template = loader.get_template('modeleditor/new.html')
    context = RequestContext(request, {
            "datasets": [{"name": "Fire unit responses", 
                          "icon": "glyphicons_022_fire.png",
                          },
                         {"name": "Tree canopy",
                          "icon": "glyphicons_317_tree_deciduous.png",
                          },
                         {"name": "Employment rates", 
                          "icon": "glyphicons_040_stats.png",
                          },
                         {"name": "Police officer presence", 
                          "icon": "glyphicons_257_sheriffs_star.png",
                          },
                         {"name": "Unsolved murders",
                          "icon": "glyphicons_290_skull.png",
                          },
                         {"name": "Stree gang members",
                          "icon": "glyphicons_043_group.png",
                          },
                         {"name": "Bus transits",
                          "icon": "glyphicons_031_bus.png",
                          },
                         {"name": "Homeless shelters",
                          "icon": "glyphicons_020_home.png",
                          },
                         {"name": "Average income",
                          "icon": "glyphicons_037_coins.png",
                          },
                         {"name": "Married couples",
                          "icon": "glyphicons_024_parents.png",
                          },
                         {"name": "Movie theaters",
                          "icon": "glyphicons_008_film.png",
                          },
                         ],
            })
    return HttpResponse(template.render(context))
