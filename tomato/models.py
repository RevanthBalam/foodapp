from django.db import models

# Create your models here.

class FoodItem:
    def __init__(self,name,des,price):
        self.name = name
        self.des = des
        self.price = price
        
