from django.shortcuts import redirect, render
from .forms import OrderForm, UserRegistrationForm
from .models import Book, Order, Product,Clothe,HomeAppliance,Electronic,Mobile
import datetime
from django.contrib import messages
import re
from django.conf import settings
from django.contrib.auth.decorators import login_required

curr_date = datetime.datetime.now()

for i in range(4):
    curr_date += datetime.timedelta(days=1)
    print(curr_date)
# Create your views here.

# Home
@login_required
def home(request):
    electronics=Electronic.objects.all()
    context={
        'electronics' :electronics
    }
    return render(request,'ecommerce/home.html',context)

# Registration Form

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            form=UserRegistrationForm()
            messages.success(request,f'Account Created for {username}!!')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    context={
        'form':form
    }
    return render(request,'ecommerce/register.html',context)

# Profile

def profile(request):
    
    context={
        'user':request.user
      
    }
    return render(request,'ecommerce/profile.html',context)


# Book

@login_required
def book(request):
    books=Book.objects.all()
    context={
        'books' :books
    }
    return render(request,'ecommerce/book.html',context)

@login_required
def bookcontent(request,pk):
    book=Book.objects.get(id=pk)
    context={
        'book':book
    }
    return render(request,'ecommerce/bookcontent.html',context)

# Clothe

@login_required
def clothe(request):
    clothes=Clothe.objects.all()
    context={
        'clothes' :clothes
    }
    return render(request,'ecommerce/clothe.html',context)

@login_required
def clothecontent(request,pk):
    clothe=Clothe.objects.get(id=pk)
    context={
        'model':clothe
    }
    return render(request,'ecommerce/clothecontent.html',context)

# HomeAppliance

@login_required
def homeappliances(request):
    homeappliances=HomeAppliance.objects.all()
    context={
        'homeappliances' :homeappliances
    }
    return render(request,'ecommerce/homeappliances.html',context)

@login_required
def homeappliancescontent(request,pk):
    homeappliances=HomeAppliance.objects.get(id=pk)
    context={
        'model':homeappliances
    }
    return render(request,'ecommerce/homeappliancescontent.html',context)

# Electronic

@login_required
def electronic(request):
    electronics=Electronic.objects.all()
    context={
        'electronics' :electronics
    }
    return render(request,'ecommerce/electronic.html',context)

@login_required
def electroniccontent(request,pk):
    electronic=Electronic.objects.get(id=pk)
    context={
        'model':electronic
    }
    return render(request,'ecommerce/electroniccontent.html',context)

# Mobile

@login_required
def mobile(request):
    mobiles=Mobile.objects.all()
    context={
        'mobiles' :mobiles
    }
    return render(request,'ecommerce/mobile.html',context)

@login_required
def mobilecontent(request,pk):
    mobile=Mobile.objects.get(id=pk)
    context={
        'model':mobile
    }
    return render(request,'ecommerce/mobilecontent.html',context)

@login_required
def add_to_cart_book(request,pk):
    if request.method=='GET':
        book=Book.objects.get(id=pk)
        book.quantity=book.quantity-1
        book.save()

        product=Product(
            user=request.user,
            title=book.title,
            pip=book.price,
            price=book.price,
            quantity=1,
            discount=book.discount,
            pimg=book.images
        )
        product.save()
        return redirect('bookcontent',pk=book.id)

@login_required
def add_to_cart_clothe(request,pk):
    if request.method=='GET':
        model=Clothe.objects.get(id=pk)
        model.quantity=model.quantity-1
        model.save()

        product=Product(
            user=request.user,
            title=model.title,
            pip=model.price,
            price=model.price,
            quantity=1,
            discount=model.discount,
            pimg=model.images
        )
        product.save()
        return redirect('clothecontent',pk=model.id)

@login_required
def add_to_cart_home_appliances(request,pk):
    if request.method=='GET':
        model=HomeAppliance.objects.get(id=pk)
        model.quantity=model.quantity-1
        model.save()

        product=Product(
            user=request.user,
            title=model.title,
            pip=model.price,
            price=model.price,
            quantity=1,
            discount=model.discount,
            pimg=model.images
        )
        product.save()
        return redirect('homeappliancescontent',pk=model.id)

@login_required
def add_to_cart_electronic(request,pk):
    if request.method=='GET':
        model=Electronic.objects.get(id=pk)
        model.quantity=model.quantity-1
        model.save()

        product=Product(
            user=request.user,
            title=model.title,
            pip=model.price,
            price=model.price,
            quantity=1,
            discount=model.discount,
            pimg=model.images
        )
        product.save()
        return redirect('electroniccontent',pk=model.id)

@login_required
def add_to_cart_mobile(request,pk):
    if request.method=='GET':
        model=Mobile.objects.get(id=pk)
        model.quantity=model.quantity-1
        model.save()

        product=Product(
            user=request.user,
            title=model.title,
            pip=model.price,
            price=model.price,
            quantity=1,
            discount=model.discount,
            pimg=model.images
        )
        product.save()
        return redirect('mobilecontent',pk=model.id)

@login_required
def place_order(request):
    if request.method=='GET':
        products=Product.objects.filter(user=request.user,isOrder=False)
        form=OrderForm()
        context={
            'products':products,
            'form':form
        }
        return render(request,'ecommerce/placeorder.html',context)


    if request.method=='POST':
        form=OrderForm(request.POST)
        delivery_add=request.POST['delivery_address']
       
        products=Product.objects.filter(user=request.user)
        count=Product.objects.filter(user=request.user).count()
        quantity=0
        amount=0
        for product in products:
            quantity+=product.quantity
            amount+=product.quantity*product.pip
        


        order=Order(
            user=request.user,
            delivery_address=delivery_add,
            payment_method="Cash",
            total_quantity=quantity,
            arriving_date=datetime. datetime. today() + datetime. timedelta(days=1),
            total_amount=amount,
            status="Order Today" )
        order.save()
        p=Product.objects.filter(user=request.user)
        for i in p:
            i.isOrder=True
            i.save()
       

        return redirect('place-order')


def order(request):
    if request.method=='GET':
        order=Order.objects.filter(user=request.user)
        product=Product.objects.filter(user=request.user,isOrder=True)
        context={
            'order':order,
            'products':product
        }
        return render(request,'ecommerce/order.html',context)

def cancel_order(request):
    if request.method=='GET':
        Order.objects.filter(user=request.user).delete()
        Product.objects.filter(user=request.user,isOrder=True).delete()
        return redirect('order')

@login_required
def update_product(request,pk):
    if request.method=='GET':
        product=Product.objects.get(id=pk)
        product.quantity+=1
        product.price=product.quantity*product.pip
        product.save()
        return redirect('place-order')

@login_required
def delete_product(request,pk):
    if request.method=='GET':
        Product.objects.get(id=pk).delete()
        return redirect('place-order')
