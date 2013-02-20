#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tabindex Template tag is used as a counter for tabindex attribute"""

from django import template

register = template.Library()

#@register.simple_tag
def inc(arg=None):
    "Tag giving and autoincrementing infex useful e.g. for tabindex"
    try:
        if arg is not None:
            inc.increment = arg - 1
        inc.increment += 1
        return int(inc.increment)
    except (ValueError, TypeError):
        return 1
#inc.increment = 0

register.simple_tag(inc)


def incr(value, arg=None):
    "Filter increases the value by arg."

    try:
        if arg is not None:
            inc.increment = arg - 1
        incr.increment += 1
        return int(value) + int(incr.increment)
    except (ValueError, TypeError):
        try:
            return value + 1
        except:
            return value
incr.is_safe = False

register.filter(incr)

