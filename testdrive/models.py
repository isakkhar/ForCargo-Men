from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Client(models.Model):
    """ Includes information about clients firms """

    client_name = models.CharField(_('client name'), unique=True, max_length=50)
    address = models.CharField(_('address'), max_length=200)
    contact_person = models.CharField(_('contact person'), max_length=100)
    email = models.EmailField(_('e-mail address'), max_length=85, blank=True, default='')
    phone_number = models.CharField(_('phone number'), max_length=15, blank=True, default = '')


    def __unicode__(self):
        return self.client_name

class Order(models.Model):
    """ Includes order information """

    client = models.ForeignKey(Client, related_name=_('orders'))
    order_number = models.CharField(_('order number'), unique=True, max_length=30)
    from_address = models.CharField(_('address from'), max_length=200)
    to_address = models.CharField(_('address to'), max_length=200)    
    transp_date = models.DateField(_('Day of transport.'))
    weight = models.DecimalField(_('weight'), max_digits=5, decimal_places=2)
    comments = models.CharField(_('comments'), max_length = 200, default='', blank=True)

    def __unicode__(self):
        return self.order_number

class RemarksOrder(models.Model):
    """Information about order execution"""

    order = models.OneToOneField(Order, unique=True)
    exect = models.BooleanField()
    exect_date = models.DateTimeField('Day of execution')
    details = models.CharField(max_length = 200, default='')

    def __unicode__(self):
        return self.order.order_number + " Client: " + self.order.client.client_name

