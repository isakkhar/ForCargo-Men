#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unit test for django_logistics installation  and site pages.
"""

from django.test import TestCase
import sys
import django

class InstallTest(TestCase):
    """Test installed packages"""

    def test_base_install(self):
        """Are Python, django, gettext packages installed?"""

        #Python installed and it's version >= 2.4
        self.failUnless(sys.version_info >= (2, 4))

        #Django installed
        self.assertTrue('django' in sys.modules)
        self.failUnless(django.get_version() > '1.1')

        #gettext
        self.assertTrue('gettext' in sys.modules)


class SitePagesTest(TestCase):
    """Test Home, About_us, pages"""

    def test_home(self):
        """Is Home page open"""

        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assert_("DeKaSa-Service OY car and truck repairing company" \
                                    in response.content)

    def test_about_us(self):
        """Is About us page open"""

        response = self.client.get('/aboutus/')
        self.assertEquals(response.status_code, 200)
        self.assert_("Brief history of DeKaSa-Service OY" in response.content)

