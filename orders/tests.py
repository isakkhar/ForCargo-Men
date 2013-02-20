#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
import datetime

#from django.core.urlresolvers import RegexURLPattern, reverse, resolve

class AuthOrderClient(TestCase):
    """Test that only logined client can change order status"""

    def test_auth(self):
        #available for all clients
        response = self.client.get('/orders/')
        self.assertEquals(response.status_code, 200)
        self.assert_("A week reservation table." in response.content)

#        self.client.login()
#        view, args, kwargs = resolve('/orders/2010/10/17/10:00/reserve')
#        response = self.client.get('/orders/2010/10/17/10:00/reserve', follow=True)
#        response.redirect_chain
#        print "CHAIN", response.redirect_chain
#        self.assertRedirects(response, '/accounts/login/?next=/orders/',
#                        status_code=302, target_status_code=200, msg_prefix='')

class CurrentWeek(TestCase):
    """Test orders table on current week"""

    def test_current_day(self):
        cur_date = datetime.date.today()
        response = self.client.get('/orders/')
        self.assert_(cur_date.strftime('%A %Y.%m.%d') in response.content)
        self.assertEquals(response.status_code, 200)


class ShiftCalendar(TestCase):
    """Test shift date in orders table."""

    def test_next_day(self):
        self.client.login()
        cur_date = datetime.date.today()
        nextday = cur_date + datetime.timedelta(days=1)
        response = self.client.get("/orders/" + str(nextday.year) +"/" + \
                        str(nextday.month) + "/" +str(nextday.day))
        self.assertEquals(response.status_code, 301)    #301 moved permanently

    def test_next_week(self):
        self.client.login()
        cur_date = datetime.date.today()
        nextday = cur_date + datetime.timedelta(days=7)
        response = self.client.get("/orders/" + str(nextday.year) +"/" + \
                        str(nextday.month) + "/" +str(nextday.day))
        self.assertEquals(response.status_code, 301)


