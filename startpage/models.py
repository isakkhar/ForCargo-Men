#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Classes defining SQL tables and their mappings to Python"

from django.db import models, connection
import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class InfoManager(models.Manager):
    """Auxiliary class to define complex request"""

    def visitor_number(self):
        """Count visits by hosts and time"""

#        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM startpage_requestinfo
            GROUP BY hostname, date(sestime)""")
        result_list = []
        for row in cursor.fetchall():
            numresp = row[0]
            result_list.append(numresp)
        return len(result_list)

class RequestInfo(models.Model):
    """Visitor hostnames and other info"""

    hostname = models.CharField(max_length=50)
    sestime = models.DateTimeField(default=datetime.datetime.now())
    objects = InfoManager()     # to use RequestInfo.objects.

    def __unicode__(self):
        return self.hostname

class UserProfile(models.Model):
    """ Includes information about user """

    usr = models.ForeignKey(User, verbose_name=_('user info'))
    address = models.CharField(_('address'), max_length=200)
    phone_number = models.CharField(_('phone number'), max_length=15, \
                                    blank=True, default='')
    comments = models.CharField(_('comments'), max_length=200, \
                                    blank=True, default='')

    def __unicode__(self):
        return self.usr.username
