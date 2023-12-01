from django.shortcuts import render, redirect
from django.contrib import messages
from apps.clients.models import Clients
from apps.clients.forms import ClientsForms
from apps.index.views import name_hello


def new_client(request):
    #Verifica se o usuário está logado
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('index')

    clients_form = ClientsForms() 

    if request.method == 'POST':
        clients_form = ClientsForms(request.POST)

        if clients_form.is_valid():

            company_name = clients_form.cleaned_data.get('company_name', None)
            
            #verifica se já possui um cliente cadastrado com o mesmo nome
            if company_name and Clients.objects.filter(company_name=company_name).exists():
                messages.error(request, 'Cliente já cadastrado')
            
            else:
                try:
                    clients_form.save()
                    messages.success(request, 'Novo cliente cadastrado!')
                    return redirect('index')
                except:
                    messages.error(request, 'Ocorreu um erro ao cadastrar o cliente!')
            

    name = name_hello(request)
    return render(request, 'clients.html', {'clients_form': clients_form, 'name': name})


