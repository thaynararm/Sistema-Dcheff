from django.shortcuts import render, redirect
from apps.utilities.views import name_hello, check_athentication

def index(request):
    authentication_result = check_athentication(request)

    if authentication_result:
        return authentication_result
    
    name = name_hello(request)
    return render(request, 'index.html', {'name': name})

