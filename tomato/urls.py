from django.urls import path;
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('restaurant/<int:id>',restaurant,name='rest'),
    path('cart/',cart,name='cart'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('register/',register,name='register'),
    path('owner/dashboard/',owner,name='owner'),
    path('owner/new-item',new_item,name='new-item'),
    path('owner/edit-item',edit_item,name='edit-item'),
    path('owner/view-orders',view_orders,name='view-orders'),
    path('owner/edit-profile',edit_profile,name='edit-profile'),
]
