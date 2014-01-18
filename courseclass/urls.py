from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url

# admin
#from django.contrib import admin
#admin.autodiscover()

# xadmin
import xadmin
xadmin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'admin/', include(xadmin.site.urls)),

    url(r'^accounts/', include('registration.backends.simple.urls')),
)
