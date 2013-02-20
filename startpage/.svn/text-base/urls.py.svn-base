#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Dispatcher of URIs for startpage application"

from django.conf.urls.defaults import patterns

urlpatterns = patterns('django_logistics.startpage.views',
    (r'^$', 'index'),
    (r'^aboutus/$', 'aboutus'),
    (r'^service/$', 'service'),
    (r'^prices/$', 'prices'),
    (r'^prices/prcleaning/$', 'prices', {'tpjob':'prcleaning'}),
    (r'^prices/prspecial/$', 'prices', {'tpjob':'prspecial'}),
    (r'^contacts/$', 'contacts'),
    (r'^logneed/$', 'logneed'),
    (r'^sitemap/$', 'site_map'),
)

#    (r'^orders/(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/daytable/$', \
#                            'daytable'),
#    (r'^orders/(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/daytable/(?P<hour>\d\d:\d\d)/release$', \
#                            'daytable', {'action':'release'}),
#    (r'^orders/(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/daytable/(?P<hour>\d\d:\d\d)/reserve$', \
#                            'daytable', {'anction':'reserve'}),
