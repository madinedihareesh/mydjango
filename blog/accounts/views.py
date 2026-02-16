from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import RigistrationForm,LoginForm
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.method == 'POST':
            form = RigistrationForm(request.POST)
            if form.is_valid():
                form.save()
                homeurl=reverse('home')
                return HttpResponseRedirect(homeurl)
        else:
            form = RigistrationForm()
        return render(request,'accounts/register.html',{'form':form})

def auth_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse('home'))
        form = LoginForm()
        return render(request,'accounts/login.html',{'form':form})

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))