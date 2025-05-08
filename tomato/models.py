from django.db import models

# Create your models here.

class RestaurantOwner(models.Model):
    username = models.CharField(max_length=100)
    restaurant_name = models.CharField(max_length=100)
    restaurant_image = models.ImageField(upload_to="allimages")
    password = models.CharField(max_length=100)
    restaurant_description = models.TextField()
    
    def __str__(self):
        return self.restaurant_name
    
    
class NormalUsers(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
    