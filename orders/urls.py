#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Dispatcher of URIs for orders module"

from django.conf.urls.defaults import patterns

urlpatterns = patterns('django_logistics.orders.views',
    (r'^$', 'orders'),
    (r'^(?P<mess>\w+)/$', 'orders'),
    (r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<hour>\d\d:\d\d)/release$', \
                            'daytable', {'action':'release'}),
    (r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<hour>\d\d:\d\d)/reserve$', \
                            'daytable', {'action':'reserve'}),
    (r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$', 'orders'),
    (r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<mess>\w+)/$', 'orders'),
)
