from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import*

# Create your views here.


def cart(request):
    return render(request,'cart.html')

def home(request):
    food1 = FoodItem("chineese","Eat and be Happy",50)
    food2 = FoodItem("nrmlfood","Eat and be Happy",500)
    food3 = FoodItem("bestfood","Eat and be Happy",79)
    
    
    
    return render(request,'index.html',{"foods":[food1,food2,food3]})


def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    
    res = val1+val2
    
    print(res)
    
    return render(request,'another.html',{"result":res})
    