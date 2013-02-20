#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import NoArgsCommand
from django.core import management
from django.test import simple

class Command(NoArgsCommand):

    help = "Validate test for all SiteMap links using Unicorn application"

    def handle_noargs(self, **options):

        simple.TEST_MODULE = 'testvalidation'
        management.call_command('test', 'startpage.QATest')

