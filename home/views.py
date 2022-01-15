from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth


def index(request):
    return render(request, 'home/index.html')

def handleSignupshop(request):
    # get the post parameters
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
       

        myuser = User.objects.create_user(username,password,email)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        messages.success(request,f"Congratulations, {myuser} your Morzilo account is created successfully!.......click on login to redirect the login page")
        return redirect('/')
    else:
        return HttpResponse('404-page not found')