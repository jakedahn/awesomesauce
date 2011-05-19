from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^dashboard/$', 'app.views.dashboard.index', name='dashboard_index'),
    url(r'^treemap/$', 'app.views.dashboard.treemap', name='dashboard_treemap'),
    
    url(r'^dashboard/compute/$', 'app.views.compute.index', name='compute_dashboard'),
    url(r'^dashboard/compute/instances/$', 'app.views.compute.instances', name='compute_instances'),
    url(r'^dashboard/compute/volumes/$', 'app.views.compute.volumes', name='compute_volumes'),
    url(r'^dashboard/compute/security/$', 'app.views.compute.security', name='compute_security'),
    url(r'^dashboard/compute/vpn/$', 'app.views.compute.vpn', name='compute_vpn'),

    url(r'^dashboard/objectstore/$', 'app.views.objectstore.index', name='objectstore_dashboard'),
    url(r'^dashboard/objectstore/accounts/$', 'app.views.objectstore.accounts', name='objectstore_accounts'),
    url(r'^dashboard/objectstore/rings/$', 'app.views.objectstore.rings', name='objectstore_rings'),
        
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
    )
