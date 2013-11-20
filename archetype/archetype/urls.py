from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from archetype import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'archetype.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'), 
    url(r'^modeleditor/', include('modeleditor.urls')),
    url(r'^map/', include('map.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
