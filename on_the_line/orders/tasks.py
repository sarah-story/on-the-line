from celery import task
from .models import Order
import hmac, httplib2, json, locale, datetime, urllib, requests, time
from django.http import HttpResponse

@task()
def getorders():
    access_token = 'b0y7fYe4mEiskcVybKylkw'
    request_headers = {'Authorization': 'Bearer ' + access_token,
                       'Accept': 'application/json',
                       'Content-Type': 'application/json'}
    parameters = {'limit': 1, 'order': 'DESC'}
    r = requests.get('http://connect.squareup.com/v1/me/payments?', headers=request_headers, params=parameters)
    order = r.json()[0]
    id = order['id']
    prev_order = Order.objects.latest('order_time')
    if id != prev_order.order_id:
        items_information = order['itemizations']
        print(order)
        items_list = []
        phone = ""
        for item in items_information:
            if 'notes' in item:
                note = str(item['notes'])
                if note[0] == "*":
                    phone = note[1:]
                    quantity = int(float(item['quantity']))
                    items_list.append(str(quantity) + " - " + item['name'])
                else:
                    quantity = int(float(item['quantity']))
                    items_list.append(str(quantity) + " - " + item['name'] + '<div class="note">' + item['notes'] + '</div>')
            else:
                quantity = int(float(item['quantity']))
                items_list.append(str(quantity) + " - " + item['name'])
        i = Order(items=items_list, order_time=datetime.datetime.now(), order_id=id, phone=phone)
        i.save()
