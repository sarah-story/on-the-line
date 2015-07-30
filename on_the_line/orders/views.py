from django.shortcuts import render
from hashlib import sha1
from .models import Order
from .models import Complete
import hmac, httplib2, json, locale, datetime, requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from twilio.rest import TwilioRestClient

@csrf_exempt
def order_list(request):
    orders = Order.objects.all()
    listed_order=[]
    pk_list=[]
    phone_list=[]
    for index,order in enumerate(orders):
        item_list = order.items.split(',')
        for item in item_list:
            new_item=item.replace("[", "")
            newer_item=new_item.replace("'", "")
            newest_item=newer_item.replace("]", "")
            item_list[item_list.index(item)] = newest_item
        listed_order.append(item_list)
        pk_list.append(order.pk)
        phone_list.append(order.phone)
    print(phone_list)
    return render(request, 'orders/order_list.html', {'orders': orders, 'listed_order': zip(listed_order, pk_list, phone_list)})

@csrf_exempt
def move_to_completed(request):
    if request.method == 'POST':
        pk = int(request.body)
        order = Order.objects.get(pk=pk)
        i = Complete(items=order.items, order_time=order.order_time, order_id=order.order_id, phone=order.phone)
        i.save()
        order.delete()
    return HttpResponse()

def completed_order(request):
    orders = Complete.objects.all()
    listed_order=[]
    pk_list=[]
    phone_list=[]
    for index,order in enumerate(orders):
        item_list = order.items.split(',')
        for item in item_list:
            new_item=item.replace("[", "")
            newer_item=new_item.replace("'", "")
            newest_item=newer_item.replace("]", "")
            item_list[item_list.index(item)] = newest_item
        listed_order.append(item_list)
        pk_list.append(order.pk)
        phone_list.append(order.phone)
    return render(request, 'orders/completed_order.html', {'orders': orders, 'listed_order': zip(listed_order, pk_list, phone_list)})

@csrf_exempt
def send_text(request):
    ACCOUNT_SID = "AC9d94f8ae2590dbb12145592b79c943a0"
    AUTH_TOKEN = "d4af341210130db7b13f200566cd8516"
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    if request.method == 'POST':
        number = request.body
        client.messages.create(
	        to=number,
	        from_="+18707389423",
	        body="Your order is ready!",
        )
    return HttpResponse()

