from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractUser

from CUapp.models import MyUser
from CUapp.forms import LoginForm, SignUpForm
from CUproject import settings

# Create your views here.
def index(request):
    data = settings.AUTH_USER_MODEL
    return render(request, 'index.html', {'data': data})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

def signupview(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = SignUpForm()
    return render(request, 'userpage.html', {'form':form})

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'userpage.html', {'form':form})