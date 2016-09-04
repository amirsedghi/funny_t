from django.shortcuts import render, redirect
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.db.models import Count
from . import models
from .models import Product, Address, Order, Customer, Review, Comment, OrderProduct
import math
from decimal import Decimal
from django.db.models import Count
from django.db.models import Q
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

the_user = User.objects.get(id = request.session['id'])
the_friend = User.objects.get(id = id)
Friendship.objects.create(user = the_user, friend = the_friend)
Friendship.objects.create(user = the_friend, friend = user)

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
    all_orders = Order.objects.count()
    total_page_num = math.ceil(all_orders/5.00)
    start_index = (int(id)-1)*5
    end_index = (int(id)-1)*5 + 5

    five_o = Order.objects.all().order_by('-created_at')[start_index:end_index]
    arr = []
    for a in range(1, int(total_page_num)+1):
        arr.append(a)
    context = {'orders': five_o, 'num': arr}
    return render(request, 'funt/orderdash.html', context)

def ordershow(request):
    return render(request, 'funt/ordershow.html')


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

def index(request, id):
    all_p = Product.objects.count()
    total_page_num = math.ceil(all_p/6.00)
    start_index = (int(id)-1)*6
    end_index = (int(id)-1)*6 + 6

    five_p = Product.objects.all().order_by('created_at')[start_index:end_index]
    arr = []
    for a in range(1, int(total_page_num)+1):
        arr.append(a)

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
    context = {'products': five_p, 'category': category, 'cart': sum_item, 'pages': arr}
    return render(request, 'funt/index.html', context)

def show(request, id):
    the_product = Product.objects.get(id = id)
    show_rest = Product.objects.filter(category = the_product.category).filter(~Q(id = id ))
    context = {'product': the_product, 'rest':show_rest}
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
    if len(request.POST['firstname'])<1:
        messages.error(request, "Please enter your name")
        request.session['check'] = 0
    if len(request.POST['lastname'])<1:
        messages.error(request, "Please enter your last name")
        request.session['check'] = 0
    if len(request.POST['address'])<1:
        messages.error(request, "Please enter your address")
        request.session['check'] = 0
    if len(request.POST['city'])<1:
        messages.error(request, "Please enter your city")
        request.session['check'] = 0
    if len(request.POST['state'])<1:
        messages.error(request, "Please enter your state")
        request.session['check'] = 0
    if len(request.POST['zipcode'])<1:
        messages.error(request, "Please enter your zipcode")
        request.session['check'] = 0
    if len(request.POST['billing_firstname'])<1:
        messages.error(request, "Please enter your billing name")
        request.session['check'] = 0
    if len(request.POST['billing_lastname'])<1:
        messages.error(request, "Please enter your billing last name")
        request.session['check'] = 0
    if len(request.POST['billing_address'])<1:
        messages.error(request, "Please enter your billing address")
        request.session['check'] = 0
    if len(request.POST['billing_city'])<1:
        messages.error(request, "Please enter your billing city")
        request.session['check'] = 0
    if len(request.POST['billing_state'])<1:
        messages.error(request, "Please enter your billing state")
        request.session['check'] = 0
    if len(request.POST['billing_zipcode'])<1:
        messages.error(request, "Please enter your billing zipcode")
        request.session['check'] = 0
    if request.session['check'] == 1:
        shipping_address = Address.objects.create(address = request.POST['address'], address_two = request.POST['address2'], city = request.POST['city'], state = request.POST['state'], zipcode = request.POST['zipcode'])
        billing_address = Address.objects.create(address = request.POST['billing_address'], address_two = request.POST['billing_address2'], city = request.POST['billing_city'], state = request.POST['billing_state'], zipcode = request.POST['billing_zipcode'])
        the_customer = Customer.objects.create(first_name = request.POST['firstname'], last_name = request.POST['lastname'])
        the_order = Order.objects.create(shipping_address = shipping_address, payment_address = billing_address, customer = the_customer)
        for a in request.session['addcart']:
            the_product = Product.objects.get(id = a['id'])
            current_quantity = the_product.quantity_sold
            current_quantity = current_quantity + int(a['quantity'])
            Product.objects.filter(id = a['id']).update(quantity_sold = current_quantity)
            OrderProduct.objects.create(product = the_product, order = the_order, quantity = a['quantity'])
        request.session['addcart'] = []
        return redirect('/')
    else:
        return redirect('/cart')

def redir(request):
    return redirect('/1')


def ordershow(request, id):
    the_order = Order.objects.get(id = id)
    the_products = OrderProduct.objects.filter(order = the_order)
    context = {'order': the_order, 'orderproducts': the_products }
    return render(request, 'funt/ordershow.html', context)

def showcategory(request, category):
    the_products = Product.objects.values('category').annotate(p_count = Count('category'))
    categories = Product.objects.filter(category = category)
    sum_item = 0
    # print request.session['addcart']
    if 'addcart' not in request.session:
        request.session['addcart']=[]
    for c in request.session['addcart']:
        sum_item += int(c['quantity'])
    context = {'products': the_products, 'cart': sum_item, 'categories': categories}
    return render(request, 'funt/category.html', context)


def reviews(request, id):
    the_product = Product.objects.get(id = id)
    reviews = the_product.product_review.all().order_by('-created_at')
    context = {'reviews': reviews, 'product': the_product}
    return render(request, 'funt/reviews.html', context)

def leavereview(request, id):
    the_product = Product.objects.get(id = id)
    request.session['check'] = 1
    if len(request.POST['review'])<1:
        messages.error(request, "want to leave and empty review? didn't think so ;)")
        request.session['check'] = 0
    if request.session['check'] == 1:
        Review.objects.create(review = request.POST['review'], product = the_product)
        return redirect('/reviews/' + str(id))
    else:
        return redirect('/reviews/' + str(id))

def leavecomment(request, id):
    the_review = Review.objects.get(id = id)
    the_product = the_review.product
    request.session['check'] = 1
    if len(request.POST['comment'])<1:
        messages.error(request, "want to leave and empty comment? didn't think so ;)")
        request.session['check'] = 0
    if request.session['check'] == 1:
        Comment.objects.create(comment = request.POST['comment'], review = the_review)
        return redirect('/reviews/' + str(the_product.id))
    else:
        return redirect('/reviews/' + str(the_product.id))


# the_user = User.objects.fitler(email = email)
# email = the_user[0].email
# name = the_user[0].name
# id = the_user[0].id
# if the_user:
#     # check the password
#     if passwod:
#         return True
# else:
#     return error;
