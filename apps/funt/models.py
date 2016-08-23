from __future__ import unicode_literals

from django.db import models

# Create your models here.


class product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    price = models.FloatField(max_length = 255)
    inventory = models.IntegerField(max_length = 255)
    quantity_sold = models.CharField(max_length = 255, default = 0)
    img1 = models.CharField(max_length= 255)
    img2 = models.CharField(max_length = 255)
    img3 = models.CharField(max_length= 255)
    img4 = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

class Comment(modles.Model):
    comment = modles.TextField()
    created_at = modles.DateTimeField(auto_now_add = True)

class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    address_two = models.CharField(max_length = 255, blank = True, null = True)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    zipcode = models.CharField(max_length = 5)
    billing_first_name = models.CharField(max_length = 255)
    billing_last_name = models.CharField(max_length = 255)
    billing_address = models.CharField(max_length = 255)
    billing_address_two = models.CharField(max_length = 255)
    billing_city = models.CharField(max_length = 255)
    billing_state = models.CharField(max_length = 2)
    billing_zipcode = models.CharField(max_length = 5)
    status = models.CharField(max_length = 255)
    comment = models.ForeignKey(Comment, null = True, blank = True)
