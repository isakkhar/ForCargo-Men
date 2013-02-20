from django_logistics.testdrive.models import Client, Order, RemarksOrder
from django.contrib import admin

#admin.site.register(Client)
admin.site.register(Order)
admin.site.register(RemarksOrder)

class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['client_name']}),
        ('Client information',  {'fields' : ['address', 'email']}),
        ]
admin.site.register(Client, ClientAdmin)
