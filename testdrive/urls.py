from django.conf.urls.defaults import *
from django_logistics.testdrive.models import Client

###throught Generic View
#info_dict = {
#            'queryset': Client.objects.all(),
#            }


#urlpatterns = patterns('',
#    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
#    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
#)

#--------------------------------------------------------
### throught Clients views
urlpatterns = patterns('django_logistics.testdrive.views',
     (r'^$', 'index'),
     (r'^(?P<client_id>\d+)/$', 'detail'),
     (r'^(?P<client_id>\d+)/addorder/$', 'addorder'),
     (r'^addclient/$', 'addclient'),                 
)
