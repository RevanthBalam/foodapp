from django.db import models
from django.contrib.auth.models import User,AbstractUser
from foodapplication import settings




# Create your models here.



class CustomUser(AbstractUser):
    is_owner = models.BooleanField(default=False)
    test_field = models.CharField(max_length=100, default='test')
    anotherran = models.CharField(max_length=100, default='test')
    
     

class Restaurant(models.Model):
    points_to_the_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to = {'is_owner':True},
        related_name='res',
        blank=True,
        null=True
    )
    restaurant_name = models.CharField(max_length=100)
    restaurant_image = models.ImageField(upload_to="allimages")
    restaurant_short_description = models.TextField()
    restaurant_full_description = models.TextField()
    Type_choices = [
        ('veg','veg'),
        ('Non-veg','Non-veg'),
        ('veg & Non-veg','veg-Nonveg')
    ]
    
    type_of_food = models.CharField(choices=Type_choices,default='veg',max_length=20)
    
    
    def __str__(self):
        return self.restaurant_name
   
   
class FoodItem(models.Model):
    from_the_restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='food_items',null=True,blank=True)
    food_item_image = models.ImageField(upload_to='allimages')
    food_item_name = models.CharField(max_length=30)
    food_item_price = models.CharField(max_length=30)
    food_item_des = models.TextField()
    
    def __str__(self):
        return self.food_item_name
     


# class RestaurantOwner(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
    
    
#     def __str__(self):
#         return f"{self.username} (Restaurant Owner)"
    
    
# class NormalUsers(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.username
    
    