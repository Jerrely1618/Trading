from django.shortcuts import render

def guest(request):
    return render(request,'guest/GuestHome.html')

def login(request):
    return render(request,'guest/Login.html')

def signup(request):
    return render(request,'guest/SignUp.html')
