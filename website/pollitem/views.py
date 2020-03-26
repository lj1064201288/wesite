from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib import messages
from cart.cart import Cart
from django.core.mail import send_mail

import datetime
from .models import *
from .forms import *
# Create your views here.

def index(request, cat_id=None):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    all_product = None
    all_categries = Category.objects.all()

    if cat_id is not None:
        try:
            category = Category.objects.get(id=int(cat_id))
        except:
            category = None
        if category is not None:
            all_product = Products.objects.filter(category=category)
    if all_product is None:
        all_product  = Products.objects.all().order_by('-sku')

    pagiator = Paginator(all_product, 4)
    p = request.GET.get('page')
    try:
        products = pagiator.page(p)
    except PageNotAnInteger:
        products = pagiator.page(1)
    except EmptyPage:
        products = pagiator.page(pagiator.num_pages)


    cart = Cart(request)
    temprate = get_template('myshop/index.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = temprate.render(request_content)

    return HttpResponse(html)

def product(request, product_id):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    try:
        product = Products.objects.get(id=product_id)
    except:
        product_id = None


    template = get_template('myshop/product.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(request_content)

    return HttpResponse(html)

def add_to_cart(request, product_id, quantity):
    product = Products.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.price, quantity=quantity)
    return redirect('/myshop/')

def remove_from_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

    return redirect('/myshop/cart/')

@login_required(login_url='/login')
def cart(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    all_categries = Category.objects.all()

    template = get_template('myshop/cart.html')
    cart = Cart(request)

    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(request_content)

    return HttpResponse(html)

@login_required(login_url='/login')
def order(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    all_categries = Category.objects.all()
    cart = Cart(request)
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        new_order = Order(user=user)
        form = OrderForm(request.POST, instance=new_order)

        if form.is_valid():
            order = form.save()
            email_messages = '您的购物如下: \n'
            for item in cart:
                OrderItem.objects.create(order=order, product=item.product, price=item.product.price, quantity=item.quantity)
                email_messages = email_messages + "\n" + "产品名称:{}, 价格: {}, 数量:{}.".format(item.product, item.product.price, item.quantity)
            email_messages += "\n以上共计{}元\n 小商场 \n 感谢您的订购!".format(cart.summary())
            cart.clear()
            messages.add_message(request, messages.INFO, '订单已保存,我们会尽快为您处理!')
            send_mail("感谢您的订购", email_messages, 'lj1064201288@163.com', [request.user.email],)
            send_mail('用户{}有人订购了产品'.format(request.user.username),
                      email_messages + '\n用户地址:' + request.POST.get('address'),
                      'lj1064201288@163.com', ['lj1064201288@163.com'],)
            return redirect('/myshop/myorders')
    else:
        form = OrderForm()

    template = get_template('myshop/order.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(request_content)

    return HttpResponse(html)

@login_required(login_url='/login')
def my_orders(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    all_categries = Category.objects.all()
    orders = Order.objects.filter(user=request.user)

    template = get_template('myshop/myorders.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(request_content)

    return HttpResponse(html)

