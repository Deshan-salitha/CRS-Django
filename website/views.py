from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm


# Create your views here.
def index(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST.get('password')
    #     #     Authenticate
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         messages.success(request, ('You have been logged in!'))
    #         return redirect('home')
    #     else:
    #         messages.success(request, "There was an error please try again")
    #         return redirect('home')
    # else:
    #     return render(request, 'home.html', {})
    return render(request, 'index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')
        #     Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home')
        else:
            messages.success(request, "There was an error please try again")
            return redirect('home')
    else:
        return render(request, 'index.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')


def register(request):
    return render(request, 'register.html')


def single_user_registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You have registered!'))
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'page1.html', {'form': form})
    return render(request, 'page1.html', {'form': form})


def group_registration(request):
    return render(request, 'page2.html')
