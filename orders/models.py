#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Classes defining SQL tables and their mappings to Python for Orders module"

from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class DateOrder(models.Model):
    """Order date and time"""

    client = models.ForeignKey(User, related_name=_('orders'))
    order_date = models.DateTimeField(_('Order date'), unique=True)

    def __unicode__(self):
        return self.client.username + ": " + str(self.order_date)

