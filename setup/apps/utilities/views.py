from django.shortcuts import render, redirect
from django.contrib.auth import get_user

#Verifica se o usuário está logado
def check_athentication(request):
    if not request.user.is_authenticated:
            return redirect('login')
    return None

#Retorna o primeiro e último nome do usuário -> usado para adicionar no header
def name_hello(request):
    if request.user.is_authenticated:
        user = get_user(request)
        if user:
            full_name = user.get_full_name().split()
            first_name = full_name[0]
            last_name = full_name[-1]
            name = f'{first_name} {last_name}'

        return name
