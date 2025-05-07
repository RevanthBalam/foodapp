from django.urls import path;
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('restaurant/',restaurant,name='rest'),
    path('cart/',cart,name='cart'),
    path('owner/dashboard/',owner,name='owner'),
    path('owner/new-item',new_item,name='new-item'),
    path('owner/edit-item',edit_item,name='edit-item'),
    path('owner/view-orders',view_orders,name='view-orders'),
]
