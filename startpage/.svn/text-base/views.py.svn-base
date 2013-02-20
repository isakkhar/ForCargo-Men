#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Web presentation classes"""

from django import template
from django_logistics.startpage.models import RequestInfo
from django.shortcuts import render_to_response
#                            , get_list_or_404, get_object_or_404
from django.utils.translation import ugettext as _
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache

#-------------------------------------------------------------------------------
@never_cache
def index(request):
    """
    Include the general information for Home page.

    Google Map links for all users.
    Number of hits, number of ip-addresses, visitor number are available only
    for admin.
    """ 

    title= _('Home')
    numtitle = _('Number of hits: ')
    iptitle = _('Number of ip-addresses: ')
    vnumtitle = _('Visitor number: ')
    req = RequestInfo(hostname=request.get_host())
    req.save()
    hitnum = RequestInfo.objects.count()    #hitnumber

    #calculate the number of diff. ip-addresses
    #ipnum = RequestInfo.objects.aggregate(Count('hostname', distinct=True))
    #["hostname__count"]
    ipnum = RequestInfo.objects.values('hostname').distinct().count()

    #calculate visitors number grouped by hostname and date
    #vnum = InfoManager().visitor_number()   need import InfoManager
    vnum = RequestInfo.objects.visitor_number()

    return render_to_response('infostatic/index.html',
                              { 'title': title,
                                'numtitle': numtitle,
                                'hitnum': hitnum,
                                'iptitle': iptitle,
                                'ipnum': ipnum,
                                'vnumtitle': vnumtitle,
                                'vnum': vnum,
                              },
                              context_instance=template.RequestContext(request))

#-------------------------------------------------------------------------------
# max_age=3600 is suitable only for static pages
@cache_control(must_revalidate=True, max_age=3600)
def logneed(request):
    """
    Explain why login is needed.
    """

    title = _('Why login is required?')
    return render_to_response('infostatic/logneed.html',
                              {'title': title,
                              },
                              context_instance=template.RequestContext(request))


#-------------------------------------------------------------------------------
@cache_control(must_revalidate=True, max_age=3600)
def aboutus(request):
    """
    Presents information about company stuff."
    """

    title = _('All about DeKaSa-Service OY company')
    return render_to_response('infostatic/about_us.html',
                              {'title': title
                              },
                              context_instance=template.RequestContext(request))

#-------------------------------------------------------------------------------
@cache_control(must_revalidate=True, max_age=3600)
def service(request):
    """
    Describe all kinds of company services and works.

    List of works and list of extra work are rendered in service.html template.
    """

    title = _('List of services available at DeKaSa-Service OY')
    allworks = [_('Scheduled maintenance'), _('Oil change'), _('Rustproof'), \
                _('Sharing belt change'), _('Wheels change'), \
                _('Tires balancing'), _('Tire storage'), \
                _('Inspection services'), _('Other installation/repairs')]

    extrawrk = [_('Fetching you car and returning it back'), \
                _('Cleaning service'), _('Fixing electrical problems'), \
                _('Hydraulic hose repair'), _('Welding works'), \
                _('Brake repairs'), _('Coupling change')]

    return render_to_response('infostatic/service.html',
                              {'title': title,
                               'allworks': allworks,
                               'extrawrk': extrawrk,
                              },
                              context_instance=template.RequestContext(request))

#-------------------------------------------------------------------------------
@cache_control(must_revalidate=True, max_age=3600)
def prices(request, tpjob=None):
    "Show an example of prices"

    title = _('Price List')
    prlist = [("prcleaning", _('Cleaning services')), \
              ("prspecial", _('Special offer'))]
    extext = _(u'Price of hour work is 50€ for cars and 60€ + VAT for ' \
               'others. Subsections present some other prices.')
    prcln = []
    prspcl = None
    if tpjob == "prcleaning":
        extext = ''
        prcln = [(_('Washing by hand '), u'15.00€', u'20.00€'), \
                 (_('Waxing'), u'40.00€', u'60.00€'), \
                 (_('Polishing'), u'90.00€', u'120.00€'), \
                 (_('Hard waxing'), u'80.00€', u'100.00€'), \
                 (_('Engine cleaning'), u'25.00€', u'25.00€'), \
                 (_('Vacuum cleaning'), u'10.00€', u'10.00€'), \
                 (_('Inner cleaning'), u'40.00€', u'40.00€'), \
                 (_('Couch washing'), u'45.00€', u'45.00€'), \
                 (_('Complete inner cleaning'), u'110.00€', u'110.00€'), \
                 (_('Leather cleaning'), u'35.00€', u'45.00€'), \
                 (_('Complete cleaning'), u'200.00€', u'230.00€'), \
                 (_('Label removing'), _('call'), _('call'))]
    elif tpjob == "prspecial":
        extext = ''
#        prspcl = _('No special prices at the moment.')
        prspcl = [(_('Scheduled maintenance'), _('from'), u'85.00€'),
                   (_('Winter maintenance'), _('from'), u'120.00€')]

    return render_to_response('infostatic/prices.html',
                              {'title': title,
                               'prlist': prlist,
                               'extext': extext,
                               'prcln': prcln,
                               'prspcl': prspcl,
                              },
                              context_instance=template.RequestContext(request))

#-------------------------------------------------------------------------------
@cache_control(must_revalidate=True, max_age=3600)
def contacts(request):
    "Redirect to a static page for now"

#    lnk1 = "http://maps.google.fi/maps?f=q&source=embed&hl=fi&" + \
#           "q=Lyhtykuja+6,+00740+Helsinki&sll=60.277202,25.013427&" + \
#           "sspn=0.015788,0.043731&ie=UTF8&cd=2&geocode=FdnElwMdVKV9AQ&" + \
#           "split=0&hq=&hnear=Lyhtykuja+6,+00740+Helsinki&ll=60.284047," + \
#           "25.015783&spn=0.014891,0.036478&z=14&iwloc=A"
    lnk1 = "http://maps.google.com/maps/ms?hl=en&doflg=ptm&ie=UTF8&msa=0&" + \
           "msid=207038907021923187267.00047f069be629ecba8de&" + \
           "ll=60.25655,25.075006&spn=0.031596,0.106087&z=14"
    title = _('Contact information')
    return render_to_response('infostatic/contacts.html',
                              {'title': title,
                                'lnk1':lnk1,
                              },
                              context_instance=template.RequestContext(request))

#-------------------------------------------------------------------------------
@cache_control(must_revalidate=True, max_age=3600)
def site_map(request):
    "Show list of all site links"

    title = _('Site map')
    link_list = [ ('','Site pages in English', '0'),
                  ('/', 'Home', '1'),
                  ('/accounts/register/', 'Registration', '1'),
                  ('/logneed/', 'Why login is required?', '1'),
                  ('/accounts/login/', 'Login', '1'),
                  ('/accounts/password/change/', 'Change password', '1'),
                  ('/accounts/password/reset/', 'Reset password', '1'),
                  ('/accounts/logout/', 'Log out', '1'),
                  ('/aboutus/', 'About us', '1'),
                  ('/service/', 'Services', '1'),
                  ('/orders/', 'Orders', '1', 'Needs registration'),
                  ('/prices/', 'Prices', '1'),
                  ('/prices/prcleaning/', 'Cleaning services', '2'),
                  ('/prices/prspecial/', 'Special offer', '2'),
                  ('/contacts/', 'Contacts', '1'),
#                  ('/admindks/', 'DeKaSa Administration',
#                                '1', 'Available only for site administrators'),
#                  ('/django_logistics/admin/doc/', 'Documentation',
#                                '1', 'Available only for site administrators'),
                  ('','Страницы сайта на русском языке', '0'),
                  ('/ru/', 'Начало', '1'),
                  ('/ru/accounts/register/', 'Регистрация', '1'),
                  ('/ru/logneed/', 'Почему требуется регистрация?', '1'),
                  ('/ru/accounts/login/', 'Войти', '1'),
                  ('/ru/accounts/password/change/', 'Изменить пароль', '1'),
                  ('/ru/accounts/password/reset/',
                                'Переустановить пароль', '1'),
                  ('/ru/accounts/logout/', 'Выйти', '1'),
                  ('/ru/aboutus/', 'О нас', '1'),
                  ('/ru/service/', 'Услуги', '1'),
                  ('/ru/orders/', 'Заказы', '1', 'Необходима регистрация'),
                  ('/ru/prices/', 'Цены', '1'),
                  ('/ru/prices/prcleaning/', 'Мойка и чистка', '2'),
                  ('/ru/prices/prspecial/', 'Специальное предложение', '2'),
                  ('/ru/contacts/', 'Контактная информация', '1'),
                  ('','Sivut suomeksi', '0'),
                  ('/fi/', 'Etusivu', '1'),
                  ('/fi/accounts/register/', 'Rekisteröityminen', '1'),
                  ('/fi/logneed/', 'Miksi kirjautuminen tarvitaan?', '1'),
                  ('/fi/accounts/login/', 'Kirjaudu sisään', '1'),
                  ('/fi/accounts/password/change/', 'Vaihda salasana', '1'),
                  ('/fi/accounts/password/reset/',
                                'Asettaa salasana uudelleen', '1'),
                  ('/fi/accounts/logout/', 'Kirjaudu ulos', '1'),
                  ('/fi/aboutus/', 'Henkilöstö', '1'),
                  ('/fi/service/', 'Palvelut', '1'),
                  ('/fi/orders/', 'Tilaukset', '1', 'Rekisteröinti vaaditaan'),
                  ('/fi/prices/', 'Hinnat', '1'),
                  ('/fi/prices/prcleaning/', 'Puhdistuspalvelut', '2'),
                  ('/fi/prices/prspecial/', 'Erikoistarjous', '2'),
                  ('/fi/contacts/', 'Yhteystiedot', '1'),
                ]

    return render_to_response('infostatic/sitemap.html',
                              {'title': title,
                                'link_list': link_list,
                              },
                              context_instance=template.RequestContext(request))
