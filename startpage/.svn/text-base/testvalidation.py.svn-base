#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unit test for django_logistics project.W3C Quality Assurance tools are used.
All django_logistics links pass throught Unicorn - W3C's Unified Validator."""

from django.test import TestCase
import urllib2

class QATest(TestCase):
    """QA for Dekasa-Service pages"""

    def test_general_conformance(self):
        """Performs as many checks as possible.By URI"""

        uri_base = 'dekasa-service.eu'
        uri_list = ['', '/accounts/register',
                    '/logneed',
                    '/accounts/login',
                    '/accounts/password/change',
                    '/accounts/password/reset',
                    '/accounts/logout',
                    '/aboutus',
                    '/service',
                    '/orders',
                    '/prices',
                    '/prices/prcleaning',
                    '/prices/prspecial',
                    '/contacts',
                    '/ru',
                    '/ru/accounts/register',
                    '/ru/logneed',
                    '/ru/accounts/login',
                    '/ru/accounts/password/change',
                    '/ru/accounts/password/reset',
                    '/ru/accounts/logout',
                    '/ru/aboutus',
                    '/ru/service',
                    '/ru/orders',
                    '/ru/prices',
                    '/ru/prices/prcleaning',
                    '/ru/prices/prspecial',
                    '/ru/contacts',
                    '/fi',
                    '/fi/accounts/register',
                    '/fi/logneed',
                    '/fi/accounts/login',
                    '/fi/accounts/password/change',
                    '/fi/accounts/password/reset',
                    '/fi/accounts/logout',
                    '/fi/aboutus',
                    '/fi/service',
                    '/fi/orders',
                    '/fi/prices',
                    '/fi/prices/prcleaning',
                    '/fi/prices/prspecial',
                    '/fi/contacts',]

        for elem in uri_list:
            uri = "http://validator.w3.org/unicorn/check?ucn_uri=" + uri_base \
                + elem + "%2F&ucn_task=conformance#"
            for line in urllib2.urlopen(uri):
                if "This document has not passed the test:" in line:
                    msg = "Test is not passed"
                    self.assertEqual(elem, msg)
#                elif "This document has not passed the test: W3C CSS " + \
#                                                "Validator" in line:
#                    msg = "Has not passed the test: W3C CSS Validator"
#                    self.assertEqual(elem, msg)

