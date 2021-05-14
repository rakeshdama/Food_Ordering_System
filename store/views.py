import datetime

from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import *


# Create your views here.

def menu(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'order_type': False}
        items = []
        cartItems = order['get_cart_items']

    products = Item.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'stores/menu.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'order_type': False}
        items = []
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'stores/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'order_type': False}
        items = []
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'stores/checkout.html', context)


def about(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'order_type': False}
        items = []
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'stores/about.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Item.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, item=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    trasaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = trasaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.delivery:
            DeliveryInfo.objects.create(
                customer=customer,
                order=order,
                address=data['delivery']['address'],
                city=data['delivery']['city'],
                state=data['delivery']['state'],
                zip_code=data['delivery']['zip_code'],
            )
    else:
        print("User is not logged in..")
    return JsonResponse('Payment Complete', safe=False)
