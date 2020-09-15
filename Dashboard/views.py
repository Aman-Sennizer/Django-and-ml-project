from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from predict.models import PredictionResults


@login_required(login_url='/Account/login')
def dashboard(request):
    name = request.user.username
    data = PredictionResults.objects.filter(user=name)
    return render(request, 'dashboard.html', {'dataset': data})


@login_required(login_url='/Account/login')
def logoutuser(request):
    logout(request)
    return redirect('/Account/login')
