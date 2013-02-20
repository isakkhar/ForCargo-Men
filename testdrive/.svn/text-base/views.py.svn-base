from django import template
from django.template import Context, loader
from django_logistics.testdrive.models import Client, Order
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets
from django.utils.translation import ugettext as _
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

def show(obj):
    '''Debugging tool: show everything about obj'''
    print 'show_obj:', obj
    for ii in dir(obj):
        print '  show_dir(obj):', ii, ':', getattr(obj, ii)

##class OrderForm(forms.Form):
##    order_number = forms.CharField(max_length=30)
##    from_address = forms.CharField(max_length=70)
##    to_address = forms.CharField(max_length=70)
##    transp_date = forms.DatetimeField()
##    #transp_date1 = forms.SplitDateTimeField()
##    weight = forms.IntegerField(max_value=5000)

class OrderForm(ModelForm):
    class Meta:
        model = Order
        #not show drop select list
        exclude = ('client')

class ClientForm(ModelForm):
    class Meta:
        model = Client

    def clean(self):
        if (self.cleaned_data.has_key('email') and self.cleaned_data.has_key('phone_number')
            and self.cleaned_data['email'] == '' and self.cleaned_data['phone_number'] == ''):
            raise forms.ValidationError('Enter at least e-mail address or phone number.')
        return self.cleaned_data

#---------------------------------------------------------------------------
def index(request):
    #cong = "Is the srart page advertising for Artem."
    #clnts_list = Client.objects.all()
    clnts_list = Client.objects.all()
    #print "FULL_PATH"
    #print request.get_full_path()
    #print request.user.is_authenticated()
    if request.user.is_authenticated():
        title = _('List of the clients')
        return render_to_response('clients/index.html',
                                  {'title':title,
                                  'clnts_list': clnts_list,
                                  }, context_instance=template.RequestContext(request))
    else:
        return HttpResponse("You must!! log in! Log in window under develop.")
        #return HttpResponseRedirect("/admin/")
        #return render_to_response('admin/login.html',)

#---------------------------------------------------------------------------
def detail(request, client_id):
    if request.user.is_authenticated():
        cl = get_object_or_404(Client, pk=client_id)
        act = "../" + client_id + "/addorder/"
        return render_to_response('clients/detail.html',
                                {'cl': cl,
                                'act': act,
                                 }, context_instance=template.RequestContext(request))
    else:
        return HttpResponse("You must log in! Log in window under develop.")

#---------------------------------------------------------------------------
def addorder(request, client_id):
    if request.user.is_authenticated():
        cl = get_object_or_404(Client, pk=client_id)
        msg = _('New order is saved')
        title = _('Client ') + cl.client_name + _(' can add new order.')
        if request.method == 'POST':
            form = OrderForm(request.POST)
            form.fields["transp_date"].widget = widgets.AdminDateWidget()
        #show(form)
            if form.is_valid():
                order = Order(client=cl, **form.cleaned_data)
                order.save()
                return render_to_response('clients/savemsg.html',
                                          {'cl': cl,
                                           'msg': msg,
                                          }, context_instance=template.RequestContext(request))
        else:
            form = OrderForm()
            form.fields["transp_date"].widget = widgets.AdminDateWidget()
        act = "/clients/" + client_id + "/addorder/"
        return render_to_response('clients/addorder.html',
                                       {'form': form,
                                       'title':title,
                                       'cl': cl,
                                       'act': act,
                                        }, context_instance=template.RequestContext(request))
    else:
        return HttpResponse("You must log in! Log in window under develop.")


#request.META['REMOTE_ADDR']
#---------------------------------------------------------------------------
def addclient(request):
    if request.user.is_authenticated():
        title = _('Add a new client')
        if request.method == 'POST':
            msg = _('New client is saved')
            form = ClientForm(request.POST)
            if form.is_valid():
                #cl = Client(**form.cleaned_data)
                #cl.save()
                new_client = form.save()                        
                return render_to_response('clients/savemsg.html',
                                          {#'cl':new_client,
                                           'msg': msg, 
                                          }, context_instance=template.RequestContext(request))
        else:
            form = ClientForm()
        return render_to_response('clients/addclient.html',
                                  {'form': form,
                                  'title':title,
                                  }, context_instance=template.RequestContext(request))
    else:
        return HttpResponse("You must log in! Log in window under develop.")


