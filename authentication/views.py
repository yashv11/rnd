from django.shortcuts import render,redirect,render_to_response

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages




def registerpage(request):
    return render(request,'authentication/registerpage.html')


def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user=auth.authenticate(username=email,password=password)
        print(user)

        if user is not None:
            auth.login(request,user)
            return render(request,'authentication/homepage.html')
        else:
            messages.info(request,'invalid credentials')
            return redirect('index')
    else:
        return render(request,'authentication/index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=email).exists():
            messages.info(request,'Email taken')
            return redirect('registerpage')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Alredy taken')
            return redirect('registerpage')
        else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=email,password=password,email=email)
            user.save()
            print('user created')
       
        return redirect('index')
    else:
        return render(request,'authentication/registerpage.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def homepage(request):
    return render(request,'authentication/homepage.html')



     
     


