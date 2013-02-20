#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Web presentation classes for Orders module"""

from django import template
from django_logistics.orders.models import DateOrder
from django.db import DatabaseError
from django.shortcuts import render_to_response, redirect
from django.utils.translation import ugettext as _
import datetime
from django.http import HttpResponse
from django.views.decorators.cache import never_cache

#from django.views.decorators.csrf import csrf_protect    (Django v.1.2)

#-----------------------------------------------------------------------------
def order_times(args, args1, user_name, base_path=""):
    """
    Return list (time, path, state, css_class)

    Time is list of the equal values from args and arg1 arrays. If there no
    equal values, then all time values are from args array. Colors are defined
    by order state.
    """

    chs = []
    for _ii in args:
        if args1.__len__() != 0:
            for _jj in args1:
                if _ii == _jj[0]:
                    if user_name == _jj[1]:
                        act = base_path + _ii + "/release"
                        elem = [_ii, act, _('Reserved'), "green"]
                    else:
                        act = ""
                        elem = [_ii, act, _('Occupied'), "red"]
                    break
                else:
                    act = base_path + _ii + "/reserve"
                    elem = [_ii, act, _('Available'), "blue"]
        else:
            act = base_path + _ii + "/reserve"
            elem = [_ii, act, _('Available'), "blue"]
        chs.append(elem)
    return chs

#-------------------------------------------------------------------------------
def reserve(year, month, day, hour, username, messages):
    "Order reservation depends on user registration and time."

    ordt = datetime.datetime(int(year), int(month), \
                       int(day), int(hour[0:2]), int(hour[3:5]))
    if datetime.datetime.now() < ordt:
        neword = DateOrder(client=username, \
                            order_date=ordt.isoformat(' '))
        try:
            neword.save()
        except DatabaseError:
            messages.append(_('ERROR: reserve function, saving order in DB'))
    else:
        messages.append(_('You can not change the past'))

#-------------------------------------------------------------------------------
def release(year, month, day, hour, username, messages):
    "Order cancellation depends on user registration and time."

    ordt = datetime.datetime(int(year), int(month), \
                       int(day), int(hour[0:2]), int(hour[3:5]))
    if datetime.datetime.now() < ordt:
        order = DateOrder.objects.filter(client=username, \
                                 order_date=ordt.isoformat(' '))
        try:
            order.delete()
        except DatabaseError:
            HttpResponse(_('ERROR: release function, deleting order from DB'))
    else:
        messages.append(_('You can not change the past'))


#-------------------------------------------------------------------------------
#@csrf_protect  (Django v.1.2)
# in Django v.1.2 messages will be implemented via The messages framework instead
# mess parameter
@never_cache
def orders(request, year=None, month=None, day=None, mess=None):
    "A week schedule of time available for reserving"

    cur_date = datetime.date.today()
    if year and month and day:
        start = datetime.date(int(year), int(month), int(day))
    else:
        start = cur_date

    week_end = start + datetime.timedelta(days=7)
    nextday = start + datetime.timedelta(days=1)
    prev_day = start - datetime.timedelta(days=1)
    prev_week = start - datetime.timedelta(days=7)

    daytimes = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', \
                '14:00', '15:00', '16:00', '17:00']

    title = _('A week reservation table.')

    date = DateOrder.objects.filter( \
                order_date__range=(start-datetime.timedelta(days=1), \
                                   week_end)).order_by('order_date')

    chs_list = []
    days_render = []
    while start < week_end:
        time = [(_ii.order_date.time().strftime("%H:%M"), _ii.client.username) \
             for _ii in date if _ii.order_date.date()==start]
        base_act = start.strftime("/orders/%Y/%m/%d/")
        chs = order_times(daytimes, time, request.user.username, base_act)
        chs_list.append((start, chs))
        days_render.append((start.strftime('%A %Y.%m.%d')))
        start += datetime.timedelta(days=1)
    chs_tmp = [[chs[1][ind] for chs in chs_list] \
                                        for ind in range(len(daytimes))]
    chs_render = zip(daytimes, chs_tmp)

    messages = []
    if mess:
        messages.append(_('You can not change the past'))

    return render_to_response('orders/daytable.html',
                  { 'title': title,
                    'chs_render': chs_render,
                    'days_render': days_render,
                    'path_next_day': nextday.strftime("/orders/%Y/%m/%d/"),
                    'path_prev_day': prev_day.strftime("/orders/%Y/%m/%d/"),
                    'path_next_week': week_end.strftime("/orders/%Y/%m/%d/"),
                    'path_prev_week': prev_week.strftime("/orders/%Y/%m/%d/"),
                    'messages': messages,
                    },
                  context_instance=template.RequestContext(request))

#-------------------------------------------------------------------------------
#@csrf_protect  (Django v.1.2)
@never_cache
def daytable(request, year, month, day, hour, action):
    "A table of time available for reserving"

    messages = []
    if action == "reserve":
        if request.user.is_authenticated():
            username = request.user
            reserve(year, month, day, hour, username, messages)
        else:
            return redirect('/accounts/login/?next=/orders/')
    elif action == "release":
        if request.user.is_authenticated():
            username = request.user
            release(year, month, day, hour, username, messages)
        else:
            return redirect('/accounts/login/?next=/orders/')

    #return to the last page
    last = request.REQUEST.get('next', None)
    if not last:
        last = request.META.get('HTTP_REFERER', None)
    if not last:
        last = '/orders/'

    #remove mess from URI and add again if need
    cntr = last.find('past/')
    if cntr > 0:
        last = last[:cntr]
    if messages:
        last += 'past/'

    return redirect(last)

