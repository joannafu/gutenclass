from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView

import xadmin
xadmin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'admin/', include(xadmin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
