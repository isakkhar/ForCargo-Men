#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Module with functions common to whole project."""

from django.views import i18n
from django.conf import settings
from django.http import HttpResponse, HttpResponseServerError, \
                        HttpResponseNotFound
from django.template import Context, RequestContext, loader
from django.utils.translation import ugettext as _
from django.shortcuts import redirect


def setlang(request, lng='en'):
    "Function is used for translation in case of GET method."

    if lng in [jj[0] for jj in settings.LANGUAGES]:
        if hasattr(request, 'session'):
            request.session['django_language'] = lng
        else:
            return HttpResponse("No '.session' at " + request.path).set_cookie(
                                        settings.LANGUAGE_COOKIE_NAME, lng)
    else:
        t = loader.get_template('404.html')
        msg = _('No translation for language %s.') % lng
        return HttpResponseNotFound(t.render(RequestContext(request, \
                                {'request_path': request.path, 'msg': msg})))

    return i18n.set_language(request)

def page_under_develop(request):
    """
    Customized handler500
    """

    dev_page = ["/admindks/", "/admin/doc/", "/admindks/password_chage/",
                "admindks/logout/"]

    msg = _('Sorry, this page is not ready yet.')

    if request.path in dev_page:
        t = loader.get_template('404.html')
        return HttpResponseNotFound(t.render(RequestContext(request, \
                                {'request_path': request.path, 'msg': msg})))
    else:
        t = loader.get_template('500.html')
        return HttpResponseServerError(t.render(Context({})))

