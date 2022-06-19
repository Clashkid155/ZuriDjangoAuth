from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from Lesson.forms import SignUpForm


@login_required
def home(request):
    user = request.user
    return render(request, 'ZuriTeam/home.html', {'username': user})


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = SignUpForm(request.POST)  # UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm()  # UserCreationForm()
            return render(request, 'ZuriTeam/register.html', {'form': form})
    else:
        form = SignUpForm()  # UserCreationForm()
        return render(request, 'ZuriTeam/register.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm(request.POST)
            print(form.errors, form.error_messages)
            return render(request, 'ZuriTeam/index.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'ZuriTeam/index.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('signin')
