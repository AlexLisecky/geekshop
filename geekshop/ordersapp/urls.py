app_name = "ordersapp"

import ordersapp.views as ordersapp
from django.urls import re_path,path

app_name="ordersapp"

urlpatterns = [
   path(r'^$', ordersapp.OrderList.as_view(), name='orders_list'),
   path(r'^forming/complete/(?P<pk>\d+)/$', ordersapp.order_forming_complete, name='order_forming_complete'),
   path(r'^create/$', ordersapp.OrderItemsCreate.as_view(),name='order_create'),
   path(r'^read/(?P<pk>\d+)/$', ordersapp.OrderRead.as_view(),name='order_read'),
   path(r'^update/(?P<pk>\d+)/$', ordersapp.OrderItemsUpdate.as_view(),name='order_update'),
   path(r'^delete/(?P<pk>\d+)/$', ordersapp.OrderDelete.as_view(),name='order_delete'),
]