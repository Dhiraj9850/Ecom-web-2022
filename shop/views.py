# from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth  import authenticate,login,logout
from .models import Product

def index(request):
    Products = Product.objects.all()
    print(Products)
    params = {'product':Products}  
    return render(request, 'shop/index.html',params)

def handleLoginshop(request):
	if request.user.is_authenticated:
		return redirect('shop')
	else:
		if request.method == 'POST':
			loginusername = request.POST.get('loginusername')
			loginpassword =request.POST.get('loginpassword')

			myuser = authenticate(request, username=loginusername, password=loginpassword)

			if myuser is not None:
				login(request, myuser)
				return redirect('/shop/')
				messages.success(request, f"{myuser} ,Successfully Logged In")
               
            
			else:
				messages.error(request, 'Username OR password is incorrect')

	

	
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/shop/')
