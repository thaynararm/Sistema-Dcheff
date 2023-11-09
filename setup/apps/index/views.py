from django.shortcuts import render
from django.contrib.auth import get_user

def index(request):
    name = name_hello(request)
    return render(request, 'index.html', {'name': name})

def name_hello(request):
    user = get_user(request)
    if user:
        full_name = user.get_full_name().split()
        first_name = full_name[0]
        last_name = full_name[-1]
        name = f'{first_name} {last_name}'

    return name
