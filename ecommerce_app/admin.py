from django.contrib import admin

from .models import Book,Clothe,HomeAppliance,Electronic,Mobile,Order,Product

# Register your models here.

admin.site.register(Book)
admin.site.register(Clothe)
admin.site.register(HomeAppliance)
admin.site.register(Electronic)
admin.site.register(Mobile)
admin.site.register(Order)
admin.site.register(Product)