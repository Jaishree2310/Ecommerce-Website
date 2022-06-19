from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
BOOKS_CHOICES=(
    ('fiction','Fiction'),
    ('literature','Literature'),
    ('stories','Stories'),
    ('historical','Historiacal'),
    ('geographical','geographical')
)

class  Book(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    publisher_name=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    published_date=models.DateTimeField(auto_now_add=True, blank=True)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    quantity=models.PositiveIntegerField()
    discount=models.DecimalField(max_digits=7, decimal_places=2)
    category=models.CharField(
        choices=BOOKS_CHOICES,
        max_length=100,
        default='fiction'
        )
    images=models.ImageField(upload_to='books/')

    def __str__(self):
        return self.title

CLOTHES_CHOICES=(
    ('summer_clothes','Summer_Clothes'),
    ('winter_clothes','Winter_Clothes'),
    ('rainy_clothes','Rainy_Clothes'),
    ('wedding_clothes','Wedding_Clothes'),
    ('holidays_clothes','Holidays_Clothes'),
)
class  Clothe(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    brand=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    quantity=models.PositiveIntegerField()
    discount=models.DecimalField(max_digits=7, decimal_places=2)
    category=models.CharField(
        choices=CLOTHES_CHOICES,
        max_length=100,
        default='rainy_clothes'
        )
    images=models.ImageField(upload_to='clothes/')

    def __str__(self):
        return self.title

HOMEAPPLIANCES_CHOICES=(
    ('washimg_machine','Washing_Machine'),
    ('refrigerator','Refrigerator'),
    ('water_heater','Water_Heater'),
    ('micro_oven','Micro_Oven'),
    ('dish_washer','Dish_Washer'),
)
class  HomeAppliance(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    brand=models.CharField(max_length=100)
    manufacture_date=models.DateTimeField()
    price=models.DecimalField(max_digits=7, decimal_places=2)
    quantity=models.PositiveIntegerField()
    discount=models.DecimalField(max_digits=7, decimal_places=2)
    category=models.CharField(
        choices=HOMEAPPLIANCES_CHOICES,
        max_length=100,
        default='washimg_machine'
        )
    images=models.ImageField(upload_to='home_appliances/')

    def __str__(self):
        return self.title

ELECTRONICS_CHOICES=(
    ('television','Television'),
    ('laptop','Laptop'),
    ('personal_computer','Personal_Computer'),
    ('fan','Fan'),
    ('lights','Lights'),
)
class  Electronic(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    brand=models.CharField(max_length=100)
    manufacture_date=models.DateTimeField()
    price=models.DecimalField(max_digits=7, decimal_places=2)
    quantity=models.PositiveIntegerField()
    discount=models.DecimalField(max_digits=7, decimal_places=2)
    category=models.CharField(
        choices=ELECTRONICS_CHOICES,
        max_length=100,
        default='laptop'
        )
    images=models.ImageField(upload_to='electronics/')

    def __str__(self):
        return self.title

class  Mobile(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    brand=models.CharField(max_length=100)
    manufacture_date=models.DateTimeField()
    price=models.DecimalField(max_digits=7, decimal_places=2)
    quantity=models.PositiveIntegerField()
    discount=models.DecimalField(max_digits=7, decimal_places=2)
   
    images=models.ImageField(upload_to='mobiles/')

    def __str__(self):
        return self.title
STATUS=(
    ('Order Today','Order Today'),
    ('Shipped','Shipped'),
    ('Out For Delivery','Out For Delivery'),
    ('Arriving Tomorrow','Arriving Tomorrow'),
    ('Order Delivered','Order Delivered')
)
PAYMENT=(
    ('Cash','Cash'),
   
   
)
class Order(models.Model):
   
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    delivery_address=models.TextField()
    payment_method=models.CharField(
        choices=PAYMENT,
        max_length=100,
        default='Cash'
    )
    total_quantity=models.PositiveIntegerField()
    order_date=models.DateTimeField(auto_now_add=True)
    arriving_date=models.DateTimeField()
    total_amount=models.IntegerField()
    status=models.CharField(
        choices=STATUS,
        max_length=100,
        default='Order Today'
    )
    
   
    
class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    pip=models.DecimalField(max_digits=7, decimal_places=2)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    quantity=models.PositiveIntegerField()
    discount=models.DecimalField(max_digits=7, decimal_places=2)
    isOrder=models.BooleanField(default=False)
    pimg=models.ImageField(upload_to='product/')
    def __str__(self):
        return self.title
    

