from django.contrib import admin

from userapp.models import Cart, CartItem

# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItem)
