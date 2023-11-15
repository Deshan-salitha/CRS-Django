from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignUpFormGroup
from .models import User, Attendee, Event


# Create your views here.
def index(request):
    type = 'Single'
    events = Event.objects.all()
    attenddee = Attendee.objects.all()
    for att in attenddee:
        if att.attendee_user.id == request.user.id:
            print('in')
            type = 'Group'
            print(att.attendee_group)
            if att.attendee_group:
                print('in group')
                attenddee = Attendee.objects.filter(attendee_group=att.attendee_group)
                print(attenddee)
    return render(request, 'index.html',
                  {'type': type, 'groupmembers': attenddee, 'group': att.attendee_group, 'events': events})


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
        return render(request, 'singleUserRegisration.html', {'form': form})
    return render(request, 'singleUserRegisration.html', {'form': form})


def group_registration(request):
    form = SignUpFormGroup(request.POST, None)
    users = User.objects.all()
    if request.user.is_authenticated:
        if request.POST:
            if form.is_valid():
                form.representative_user = request.user.id
                form.save()
                messages.success(request, 'Group Registered!..')
                return redirect('home')
            else:
                messages.success(request, 'dumpAss')
        return render(request, 'groupRegistration.html', {'form': form, 'user': users})
    else:
        if request.POST:
            print(request.POST['representative_user'])
            rsu = User.objects.get(pk=request.POST['representative_user'])
            if form.is_valid():
                form.save()
                messages.success(request, 'Group Registered!..')
                return redirect('home')
            else:
                messages.success(request, form._errors)
        return render(request, 'groupRegistration.html', {'form': form, 'user': users})
