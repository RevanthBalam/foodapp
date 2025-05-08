from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth.hashers import make_password,check_password
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
    restaurants = RestaurantOwner.objects.all()
    return render(request,'index.html',{'res':restaurants})


def cart(request):
    return render(request,'cart.html')

def login(request):
    return render(request,'login.html')
def register(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        
        if password_1 == password_2:
            if NormalUsers.objects.filter(username = username).exists() or RestaurantOwner.objects.filter(username=username).exists():
                return render(request,'register.html',{'error':"Username Taken"})
            users = NormalUsers.objects.all()
            for user in users:
                isHave = check_password(password_1,user.password)
                if isHave:
                    return render(request,'register.html',{'error':"Password Taken"})
                
            users = RestaurantOwner.objects.all()
            for user in users:
                isHave = check_password(password_1,user.password)
                if isHave:
                    return render(request,'register.html',{'error':"Password Taken"})
            
            hashedpass=make_password(password_1)
            NormalUsers.objects.create(username=username,password=hashedpass)
                
            return redirect('home')
        return render(request,'register.html',{'error':"Password doesnt match"})
    return render(request,'register.html')

#displayregisterpage of owner
def register_owner(request):  
        if request.method == 'POST':
            
            username = request.POST.get('res-username')
            restaurant_name = request.POST.get('name')
            restaurant_img = request.FILES.get('res-image')
            password1 = request.POST.get('password_1')
            password2 = request.POST.get('password_2')
            res_des = request.POST.get('res-des')
            
            if (password1 == password2):
                if NormalUsers.objects.filter(username = username).exists() or RestaurantOwner.objects.filter(username=username).exists():
                    return render(request,'regitser-owner.html',{'error':"Username Taken"})
                
                users = NormalUsers.objects.all()
                for user in users:
                    isHave = check_password(password1,user.password)
                    if isHave:
                        return render(request,'regitser-owner.html',{'error':"Password Taken"})
                
                users = RestaurantOwner.objects.all()
                for user in users:
                    isHave = check_password(password1,user.password)
                    if isHave:
                        return render(request,'regitser-owner.html',{'error':"Password Taken"})
               
                hashed_password = make_password(password1)
                RestaurantOwner.objects.create(
                        username=username,
                        restaurant_name=restaurant_name,
                        restaurant_image=restaurant_img,
                        password=hashed_password,
                        restaurant_description = res_des
                        )
                return redirect('owner')
            return render(request,'regitser-owner.html',{'error':"Password not match"})
                
        print("outside")
        return render(request,'regitser-owner.html')
    