from django.contrib import admin

from app2.models import Products,Customer,Review
# Register your models here.

admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Review)