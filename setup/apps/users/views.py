from django.shortcuts import render, redirect
from apps.users.forms import LoginForms
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()

        user = auth.authenticate(
            request,
            username = username,
            password = password
        )

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    
    return render(request, 'login.html', {'form': form})
