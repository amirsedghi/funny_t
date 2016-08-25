from django.shortcuts import render, redirect
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.db.models import Count
from . import models
from .models import Product, Address, Order, Customer, Review, Comment, OrderProduct
import math
from decimal import Decimal
from django.db.models import Count
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
        return redirect('/dashboard/products/1')
    else:
        return redirect('/admin')

def productdash(request, id):
    all_p = Product.objects.count()
    total_page_num = math.ceil(all_p/5.00)
    start_index = (int(id)-1)*5
    end_index = (int(id)-1)*5 + 5

    five_p = Product.objects.all()[start_index:end_index]
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
    products_cat = Product.objects.values('category').annotate(p_count = Count('category'))
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
    products_cat = Product.objects.values('category').annotate(p_count = Count('category'))
    print "$$$$$$$$$$$$$$$$$********************$$$$$$$$$$$$$$$$$$$$"
    print products_cat.query
    print "$$$$$$$$$$$$$$$$$********************$$$$$$$$$$$$$$$$$$$$"
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
    rep_product = Product.objects.filter(name = request.POST['product_name'])
    if rep_product:
        print id
        print rep_product[0].id
        if int(id) != rep_product[0].id:
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

def index(request):
    sum_item = 0
    # print request.session['addcart']
    if 'addcart' not in request.session:
        request.session['addcart']=[]
    for c in request.session['addcart']:
        sum_item += int(c['quantity'])
    print 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

    request.session['sum_item'] = sum_item
    print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    print request.session['sum_item']
    print request.session['addcart']
    products = Product.objects.all()
    category = Product.objects.values('category').annotate(p_count = Count('category'))
    context = {'products': products, 'category': category, 'cart': sum_item}
    return render(request, 'funt/index.html', context)

def show(request, id):
    the_product = Product.objects.get(id = id)
    context = {'product': the_product}
    return render(request, 'funt/show.html', context)

def multiply(value, arg):
    return value*arg

def cart(request):
    product_cart = []
    total_price = Decimal(0.00)
    for a in request.session['addcart']:
        the_product = Product.objects.get(id = a['id'])
        total = the_product.price*Decimal(a['quantity'])
        product_cart.append([the_product, a['quantity'], total])
        total_price=total_price + total
    context = {'the_cart':product_cart, 'total': total_price}
    print '(((((((((((((((((())))))))))))))))))'
    print request.session['sum_item']
    return render(request, 'funt/cart.html', context)

def addcart(request):
    # for a in request.session['addcart']:
    #     if a['id'] == request.POST['id']:
    #         temp = a['quantity']
    #         a.update({'id':request.POST['id'], 'quantity' : str(int(request.POST['quantity'])+int(temp))})
    sessionlist = request.session['addcart']
    sessionlist.insert(0,{'id':request.POST['id'], 'quantity':request.POST['quantity']})
    request.session['addcart'] = sessionlist
    print 'BBBBBBBBBBBBBBBBBBBBBBBB'
    print request.session['addcart']
    return redirect('/')

def processorder(request):
    request.session['check'] = 1

    return redirect('/')
