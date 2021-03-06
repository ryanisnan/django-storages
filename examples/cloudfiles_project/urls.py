from django.conf import settings
from photos.models import Photo

try:
    from django.conf.urls import include, patterns
except ImportError:  # deprecated since Django 1.4
    from django.conf.urls.defaults import include, patterns  # noqa


photo_dict = {
    'queryset': Photo.objects.all()
}

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^photos/$', 'django.views.generic.list_detail.object_list', photo_dict),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )