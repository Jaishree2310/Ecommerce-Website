from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ecommerce_app.models import Order,Product

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['delivery_address','payment_method']


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['quantity']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']