#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Django url dispatch file for django_logistics project.'

#from django.conf.urls.defaults import *
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import include, handler404

from django.conf import settings

# Uncomment the next two lines to enable the admin (v.1.2.1):
# is used for developing
from django.contrib import admin
admin.autodiscover()

js_info_dict = {
    'packages': ('django_logistics',)
}

handler500 = 'django_logistics.viewtools.views.page_under_develop'

urlpatterns = patterns('',

    (r'^tools/', include('django_logistics.viewtools.urls')),

    (r'^', include('django_logistics.startpage.urls')),
    # Language code explicit in the URL
    (r'^(\w\w)/', include('django_logistics.startpage.urls')),

    (r'^orders/', include('django_logistics.orders.urls')),
    # Language code explicit in the URL
    (r'^(\w\w)/orders/', include('django_logistics.orders.urls')),

    (r'^accounts/', include('django_logistics.registration.urls')),
    # Language code explicit in the URL
    (r'^(\w\w)/accounts/', include('django_logistics.registration.urls')),

    #(r'^clients/', include('django_logistics.testdrive.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # is used for developing
    #   (r'^admindks/(.*)', admin.site.root),  # Django v.1.0
    (r'^admindks/', include(admin.site.urls)), # Django v.1.2 or v.1.3


#    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^staticfiles/css/(?P<path>.*)$', 'django.views.static.serve',
                    {'document_root': settings.STATIC_DOC_ROOT + '/css',
                     'show_indexes': True}),
        (r'^staticfiles/js/(?P<path>.*)$', 'django.views.static.serve',
                    {'document_root': settings.STATIC_DOC_ROOT + '/js',
                     'show_indexes': True}),
        (r'^staticfiles/img/(?P<path>.*)$', 'django.views.static.serve',
                    {'document_root': settings.STATIC_DOC_ROOT + '/img',
                     'show_indexes':True}),
)

