from django.contrib import admin

from .models import Cart, CartProduct

admin.site.register([Cart, CartProduct])
