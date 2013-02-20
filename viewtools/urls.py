#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Dispatcher of URIs for viewtools module"

from django.conf.urls.defaults import patterns

urlpatterns = patterns('django_logistics.viewtools.views',

    (r'^i18n/setlang/(?P<lng>.{2,})/$', 'setlang'),
)
