# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Shipping(models.Model):
    shipping_first_name = models.CharField(max_length=50)
    shipping_last_name = models.CharField(max_length=50)
    shipping_address_line1 = models.CharField(max_length=100)
    shipping_address_line2 = models.CharField(max_length=100)
    shipping_city = models.CharField(max_length=50)
    shipping_state = models.CharField(max_length=50)
    shipping_country = models.CharField(max_length=50)
    shipping_phone_number = models.CharField(max_length=20)

class Shipment(models.Model):
    retailer = models.CharField(max_length=100)
    product_id = models.CharField(max_length=50)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    quatity = models.CharField(max_length=50)










