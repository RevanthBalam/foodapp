from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import*

# Create your views here.


def restaurant(request):
    return render(request,'restaurant.html')
def owner(request):
    return render(request,'owner.html')
def new_item(request):
    return render(request,'newitem.html')
def edit_item(request):
    return render(request,'edititem.html')
def view_orders(request):
    return render(request,'vieworders.html')

def home(request):
    food1 = FoodItem("chineese","Eat and be Happy",50)
    food2 = FoodItem("nrmlfood","Eat and be Happy",500)
    food3 = FoodItem("bestfood","Eat and be Happy",79)
    
    
    
    return render(request,'index.html',{"foods":[food1,food2,food3]})


def cart(request):
    
    
    return render(request,'cart.html')
    