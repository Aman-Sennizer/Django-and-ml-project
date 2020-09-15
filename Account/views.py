from django.shortcuts import render, redirect
from django.contrib import messages
from Account.forms import CreateUserForms
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    if request.user.is_authenticated:
        return redirect('/Dashboard/Dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('/Dashboard/Dashboard')
                else:
                    messages.info(request, 'your account has been disabled \n Please login again')
                    return render(request, 'login.html')
            else:
                messages.info(request, 'Invalid Credentials')
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('/Dashboard/Dashboard')
    else:
        if request.method == 'POST':
            form = CreateUserForms(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account Successfully created for ' + user)
                return redirect('/Account/login')
            else:
                return render(request, 'register.html', {'form': form})

        else:
            form = CreateUserForms()
            return render(request, 'register.html', {'form': form})
