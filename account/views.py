from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import LoginForm,SignupForm
from rest_framework.response import Response
from .models import Signup
@login_required
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'home.html')
            #return redirect('home')
            #return HttpResponse("<html><body bgcolor=red><center>registered</center></body></html>")
        else:
            return HttpResponse("Error")
    else:
        form = UserCreationForm()
    return render(request,'signup.html', {'form': form})


def login(request):
    if request.method =='POST':
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            dbuser=authenticate(username=request.POST['user'],
                                password=request.POST['pwd'])

            if not dbuser:
                return HttpResponse('LOGIN FAILED')
            else:
                return HttpResponse('LOGIN SUCCESS')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})