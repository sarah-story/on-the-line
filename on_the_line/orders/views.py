from django.shortcuts import render
from bottle import post, request, run
from hashlib import sha1
from .models import Order
import hmac, httplib, json, locale, datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def get_orders(request):
    # access_token = 'b0y7fYe4mEiskcVybKylkw'
    # request_headers = { 'Authorization': 'Bearer ' + access_token,
    #                     'Accept': 'application/json',
    #                     'Content-Type': 'application/json'}
    # callback_body = request.body.getvalue()
    # callback_body_dict = json.loads(callback_body)
    # payment_id = callback_body_dict['entity_id']
    # connection = httplib.HTTPSConnection('connect.squareup.com')
    # connection.request('GET', '/v1/me/payments/' + payment_id, '', request_headers)
    # connect_response_body = json.loads(connection.getresponse().read())
    # items_information = connect_response_body['itemizations']
    # items_list = []
    # for item in items_information:
    #     items_list += str(round(item['quantity'])) + " " + item['name'] + "<br>"
    # i = Order(items = items_list, order_time = datetime.datetime.now())
    # i.save()
    return HttpResponse("")





