from django.shortcuts import render


def check_athentication(request):
    #Verifica se o usuário está logado
    if not request.user.is_authenticated:
            messages.error(request, 'Usuário não logado')
            return redirect('index')
