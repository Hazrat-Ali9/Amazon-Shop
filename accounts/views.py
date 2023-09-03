from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm,LoginForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def profile(request):
    return render(request,'dashboard.html')


def login_user(request):
     if request.method == 'GET':
        return render(request, 'login.html', {'form': LoginForm})
     else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'form':LoginForm,
                                                   'error': 'username and  password do no match'})
        else:
            login(request, user)
            return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('login')
