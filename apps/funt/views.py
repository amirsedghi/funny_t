from django.shortcuts import render, redirect
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.db.models import Count
from . import models
from .models import Product, Address, Order, Customer, Review, Comment
import math
from decimal import Decimal
# Create your views here.
def admin(request):
    request.session['admin'] = 0
    return render(request, 'funt/admin.html')

def login(request):
    request.session['check'] = 1
    if len(request.POST['email'])<1:
        messages.error(request, 'Email please...')
        request.session['check'] = 0
    if len(request.POST['password'])<1:
        messages.error(request, 'Password please...')
        request.session['check'] = 0
    if request.POST['email']!='admin@admin.com' or request.POST['password']!='admin':
        messages.error(request, "I'm sure you're the admin, try again buddy...")
        request.session['check'] = 0
    if request.session['check'] == 1:
        request.session['admin'] =1
        return redirect('/dashboard/orders/1')
    else:
        return redirect('/admin')

def productdash(request, id):
    all_p = Product.objects.count()
    total_page_num = math.ceil(all_p/5.00)
    start_index = (int(id)-1)*5
    end_index = (int(id)-1)*5 + 5

    five_p = Product.objects.all()[start_index:end_index]
    print '******************'
    print 'start index: ' + str(start_index)
    print 'end index:' + str(end_index)
    print five_p.query
    print 'total page: ' + str(total_page_num)
    print math.ceil(all_p/5.00)
    print '******************'
    arr = []
    for a in range(1, int(total_page_num)+1):
        arr.append(a)
    print arr
    context = {'total_page': arr, 'products': five_p}
    print all_p
    return render(request, 'funt/productdash.html', context)


def orderdash(request, id):
    return render(request, 'funt/orderdash.html')


def add(request):
    products_cat = Product.objects.values('category')
    context = {'categories': products_cat}
    return render(request, 'funt/add.html', context)

def adding(request):
    request.session['check'] = 1
    if len(request.POST['product_name'])<1:
        messages.error(request, "Name cannot be empty")
        request.session['check'] = 0
    if len(request.POST['description'])<1:
        messages.error(request, "Description cannot be empty")
        request.session['check'] = 0
    if request.POST['category'] == 'Category' and len(request.POST['new_category'])<1:
        messages.error(request, "Please pick a category")
        request.session['check'] = 0
    if len(request.POST['img_one'])<1:
        messages.error(request, "Choose an image")
        request.session['check'] = 0
    if len(request.POST['price'])<1:
        messages.error(request, "Pirce cannot be empty")
        request.session['check'] = 0
    if len(request.POST['inventory_count'])<1:
        messages.error(request, "Inventory count cannot be empty")
        request.session['check'] = 0
    rep_product = Product.objects.filter(name = request.POST['product_name'])
    if rep_product:
        messages.error(request, "This name is already taken")
        request.session['check'] = 0
    if request.POST['category'] == 'Category':
        the_category = request.POST['new_category']
    else:
        the_category = request.POST['category']
    if request.session['check'] == 1:
        Product.objects.create(name = request.POST['product_name'], price = Decimal(request.POST['price']), description = request.POST['description'], category = the_category, inventory_count = int(request.POST['inventory_count']), img_one = request.POST['img_one'], img_two = request.POST['img_two'], img_three = request.POST['img_three'], img_four = request.POST['img_four'])
        return redirect('/dashboard/products/1')
    else:
        return redirect('/add')

def edit(request, id):
    the_product = Product.objects.get(id = id)
    products_cat = Product.objects.values('category')
    context = {'p': the_product, 'categories': products_cat}
    return render(request, 'funt/edit.html', context)

def editing(request, id):
    request.session['check'] = 1
    if len(request.POST['product_name'])<1:
        messages.error(request, "Name cannot be empty")
        request.session['check'] = 0
    if len(request.POST['description'])<1:
        messages.error(request, "Description cannot be empty")
        request.session['check'] = 0
    if request.POST['category'] == 'Category' and len(request.POST['new_category'])<1:
        messages.error(request, "Please pick a category")
        request.session['check'] = 0
    if len(request.POST['img_one'])<1:
        messages.error(request, "Choose an image")
        request.session['check'] = 0
    if len(request.POST['price'])<1:
        messages.error(request, "Pirce cannot be empty")
        request.session['check'] = 0
    if len(request.POST['inventory_count'])<1:
        messages.error(request, "Inventory count cannot be empty")
        request.session['check'] = 0
    the_product = Product.objects.get(id = id)
    rep_product = Product.objects.get(name = request.POST['product_name'])
    if rep_product and the_product.name != request.POST['product_name']:
        messages.error(request, "This name is already taken")
        request.session['check'] = 0
    if request.POST['category'] == 'Category':
        the_category = request.POST['new_category']
    else:
        the_category = request.POST['category']
    if request.session['check'] == 1:
        Product.objects.filter(id = id).update(name = request.POST['product_name'], price = Decimal(request.POST['price']), description = request.POST['description'], category = the_category, inventory_count = int(request.POST['inventory_count']), img_one = request.POST['img_one'], img_two = request.POST['img_two'], img_three = request.POST['img_three'], img_four = request.POST['img_four'])
        return redirect('/dashboard/products/1')
    else:
        return redirect('/edit/'+ str(id))

def delete(request, id):
    Product.objects.filter(id = id).delete()
    return redirect('/dashboard/products/1')
