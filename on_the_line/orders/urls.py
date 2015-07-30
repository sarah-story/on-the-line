from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.order_list, name='getorders'),
    url(r'^to_completed/$', views.move_to_completed, name='movetocompleted'),
    url(r'^completed/$', views.completed_order, name='completed'),
    url(r'^text/$', views.send_text, name='text')
]