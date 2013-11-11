from django.conf.urls import patterns, url

from modeleditor import views

urlpatterns = patterns('',
    url(r'^new/$', views.new, name='new')
)
