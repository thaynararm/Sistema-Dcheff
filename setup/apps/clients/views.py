from django.shortcuts import render, redirect
from django.contrib import messages
from apps.clients.models import Clients
from apps.clients.forms import ClientsForms
from apps.utilities.views import name_hello, check_athentication


def new_client(request):    
    #Verifica se o usuário está logado
    authentication_result = check_athentication(request)

    if authentication_result:
        return authentication_result

    #Exibe e instancia o formulário
    clients_form = ClientsForms() 

    if request.method == 'POST':
        clients_form = ClientsForms(request.POST)

        new_company_name = request.POST['company_name']

        #Verifica se o nome do cliente já está cadastrado
        if Clients.objects.filter(company_name=new_company_name).exists():
            messages.error(request, 'Nome da empresa já cadastrado!')

        #Verifica se o formulário é valido e salva no banco de dados
        if clients_form.is_valid():
                try:
                    clients_form.save()
                    messages.success(request, 'Novo cliente cadastrado!')
                    return redirect('index')
                except:
                    messages.error(request, 'Ocorreu um erro ao cadastrar o cliente!')
            
    name = name_hello(request)
    return render(request, 'clients.html', {'clients_form': clients_form, 'name': name})


