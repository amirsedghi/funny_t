from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 225)
    price = models.DecimalField(decimal_places = 2, max_digits = 5)
    description = models.TextField()
    category = models.CharField(max_length = 255)
    inventory_count = models.IntegerField()
    quantity_sold = models.IntegerField(default = 0)
    img_one = models.TextField()
    img_two = models.TextField(null = True, blank = True)
    img_three = models.TextField(null = True, blank = True)
    img_four = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Address(models.Model):
    address = models.CharField(max_length = 255)
    address_two = models.CharField(max_length = 255, default='')
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 2)
    zipcode = models.CharField(max_length = 5)


class Order(models.Model):
    status = models.CharField(max_length = 255, default = 'in process')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    product = models.ManyToManyField(Product)
    shipping_address = models.OneToOneField(Address, related_name = 'sipping_add', on_delete = models.CASCADE)
    payment_address = models.OneToOneField(Address, related_name = 'payment_add', on_delete = models.CASCADE)
    cutomer = models.ForeignKey('Customer', default = 1,  related_name = 'order_customer', on_delete = models.CASCADE)

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, related_name = 'order_product', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name = 'product_order', on_delete = models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)

class Customer(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)

class Review(models.Model):
    review = models.TextField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    product = models.ForeignKey(Product, related_name = 'product_review', on_delete = models.CASCADE)

class Comment(models.Model):
    comment = models.TextField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    review = models.ForeignKey(Review, related_name = 'review_comment', on_delete = models.CASCADE)
