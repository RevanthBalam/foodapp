from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Restaurant


from .models import*

# Create your views here.



def restaurant(request,id):
    
    
    res_details = Restaurant.objects.get(id=id)
    print(res_details,"restas details 18")
    
    food_items = FoodItem.objects.filter(from_the_restaurant_id=id)
    
    print("food items 22")
    
    return render(request,'restaurant.html',{'res_details':res_details,'food_items':food_items})


def delete_item(request,id):
    
    FoodItem.objects.get(id=id).delete()
    
    return redirect('edit-item')
    
    
def add_to_cart(request,id):
    
    
    
    


def owner(request):
    
    user=request.user
    
    if request.method == "POST":
        
        this_res = Restaurant.objects.filter(points_to_the_user = request.user ).first()
        
        if this_res:
                this_res.restaurant_name = request.POST.get('res-name')
                this_res.restaurant_short_description = request.POST.get('res-short-des')
                this_res.restaurant_full_description = request.POST.get('res-long-des')
                this_res.type_of_food = request.POST.get('type_of_providing_food')
                
                
                if request.FILES.get('res-img'):
                    this_res.restaurant_image = request.FILES.get('res-img')
                    
                
                
                this_res.save()
                return redirect('owner')
        
        restaurantname = request.POST.get('res-name')
        restaurant_short_des = request.POST.get('res-short-des')
        restaurant_long_des = request.POST.get('res-long-des')
        restaurant_img = request.FILES.get('res-img')
        restaurant_type_of_food_providing = request.POST.get('type_of_providing_food')
            
        Restaurant.objects.create(restaurant_name=restaurantname,
                                  restaurant_short_description=restaurant_short_des,
                                  restaurant_full_description = restaurant_long_des,
                                  restaurant_image = restaurant_img,
                                  type_of_food = restaurant_type_of_food_providing,
                                  points_to_the_user = user
                                  )
        
        
        return render(request, 'owner.html')

    return render(request,'owner.html')



def new_item(request):
    
    if request.method == "POST":
        restaurant = Restaurant.objects.get(points_to_the_user = request.user)
        foodname = request.POST.get('foodproductname')
        food_des = request.POST.get('Description')
        food_price = request.POST.get('price')
        food_image = request.FILES.get('img')
        
        
        FoodItem.objects.create(food_item_image=food_image,
                                food_item_name=foodname,
                                food_item_price=food_price,
                                food_item_des=food_des,
                                from_the_restaurant=restaurant)
        
        return redirect('owner')
        
    return render(request,'newitem.html')




def update_item_details(request,id):
    if request.method == "POST":
        name = request.POST.get('foodproductname')
        des = request.POST.get('Description')
        price = request.POST.get('price')
        img = request.FILES.get('img')
        
        
        
    if img:
        FoodItem.objects.filter(id=id).update(
            food_item_name=name,
            food_item_price = price,
            food_item_des = des,
            food_item_image=img   
        )
        
        return redirect('owner')
    
    else:
        FoodItem.objects.filter(id=id).update(
            food_item_name=name,
            food_item_price = price,
            food_item_des = des,  
        )
        
        return redirect('owner')
    
    
        


def edit_item_details(request,id):
    
    fooddetails = FoodItem.objects.get(id=id)
    
    return render(request,'edit-item-details.html',{'fooddetails':fooddetails})


def edit_item(request):
    
    res = Restaurant.objects.get(points_to_the_user = request.user)
    
    print(res,"93 line")
    
    fooditemsofres = FoodItem.objects.filter(from_the_restaurant = res)
    
    print(fooditemsofres,"97")
     
    
    
    return render(request,'edititem.html',{'fooditems':fooditemsofres})



def view_orders(request):
    return render(request,'vieworders.html')

def home(request):
    
    rests = Restaurant.objects.all()
    return render(request,'index.html',{'rests':rests})


def cart(request):
    return render(request,'cart.html')




def edit_profile(request):
    
    res = None
    
    
    if Restaurant.objects.filter(points_to_the_user=request.user).exists():
        res = Restaurant.objects.get(points_to_the_user=request.user)
        print(res.restaurant_image,"167")

    return render(request,'res-profile.html',{'rest':res})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password=password)
        if user:
            login(request,user)
            
            if user.is_owner:
                return redirect('owner')
            else:

                return redirect('home')      
        else:
            return render(request,'login.html',{'error':'Invalid'})
        
    return render(request,'login.html')
        




def logout_view(request):
    logout(request)
    return redirect('login')



def register(request):
    
    if request.method == "POST":
        
        username = request.POST.get('user_name')
        password1 = request.POST.get('password_1')
        password2 = request.POST.get('password_2')
        
        if request.POST.get('is_owner'):
            isowner = True
        else:
            isowner = False
            
            
        if password1 == password2:
            if CustomUser.objects.filter(username = username).exists():
                return render(request,'register.html',{'error':'Username Taken'})
            CustomUser.objects.create_user(username=username,password=password1,is_owner=isowner)
            if CustomUser.is_owner:
                return redirect('login')
            return redirect('home')
    
    return render(request,'register.html')
