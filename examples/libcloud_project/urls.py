try:
    from django.conf.urls import include, patterns, url
except ImportError:  # deprecated since Django 1.4
    from django.conf.urls.defaults import include, patterns, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'libcloud_project.views.home', name='home'),
    # url(r'^libcloud_project/', include('libcloud_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
