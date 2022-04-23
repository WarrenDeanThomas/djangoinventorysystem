from django.contrib import admin
from .models import Product, Order    #Product - can include them individually or all
from django.contrib.auth.models import Group

admin.site.site_header = "Wazza Dashboard Admin"


# Below you can change the display of a model from the std display that django gives you
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ('category',)  #- here you can add a filter to the admin page - or use a list ['catgory]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
# admin.site.unregister(Group) - you can remove a model from the admin page