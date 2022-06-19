
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
   # Home Url
    path('home',views.home,name="home"),


   # Book Url
    path('book',views.book,name="book"),

   # Book-Content Url
    path('bookcontent/<int:pk>/',views.bookcontent,name="bookcontent"),

   # Clothe Url
    path('clothe',views.clothe,name="clothe"),

   # Clothe-Content Url
    path('clothecontent/<int:pk>/',views.clothecontent,name="clothecontent"),

   # homeappliances Url
    path('homeappliances',views.homeappliances,name="homeappliances"),

   # homeappliances-Content Url
    path('homeappliancescontent/<int:pk>/',views.homeappliancescontent,name="homeappliancescontent"),

    
   # electronic Url
    path('electronic',views.electronic,name="electronic"),

   # electronic-Content Url
    path('electroniccontent/<int:pk>/',views.electroniccontent,name="electroniccontent"),
    
   # mobile Url
    path('mobile',views.mobile,name="mobile"),

   # mobile-Content Url
    path('mobilecontent/<int:pk>/',views.mobilecontent,name="mobilecontent"),

   # Add To Cart  Url for Book
    path('add-to-cart-book/<int:pk>/',views.add_to_cart_book,name="add-to-cart-book"),

   # Add To Cart  Url for Clothe
    path('add-to-cart-clothe/<int:pk>/',views.add_to_cart_clothe , name="add-to-cart-clothe"),

   # Add To Cart  Url for HomeAppliance
    path('add-to-cart-homeappliances/<int:pk>/',views.add_to_cart_home_appliances,name="add-to-cart-homeappliances"),

   # Add To Cart  Url for Electronic
    path('add-to-cart-electronic/<int:pk>/',views.add_to_cart_electronic,name="add-to-cart-electronic"),

   # Add To Cart  Url for Mobile
    path('add-to-cart-mobile/<int:pk>/',views.add_to_cart_mobile,name="add-to-cart-mobile"),

   # Place Order  Url 
    path('place-order',views.place_order,name="place-order"),

   # Order  Url 
    path('order',views.order,name="order"),

     # Cancel Order  Url 
    path('cancel-order',views.cancel_order,name="cancel-order"),


   # Update Product  Url 
    path('update-product/<int:pk>/',views.update_product,name="update-product"),

   # Delete Product  Url 
    path('delete-product/<int:pk>/',views.delete_product,name="delete-product"),

        #  Registration
    path('register',views.register,name='register'),

     #  Profile
    path('profile',views.profile,name='profile'),
]
