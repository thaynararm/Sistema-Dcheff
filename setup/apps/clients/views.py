from django.shortcuts import render, redirect
from django.contrib import messages
from apps.clients.models import Clients
from apps.clients.forms import ClientsForms
from apps.index.views import name_hello


def new_client(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('index')

    clients_form = ClientsForms()

    if request.method == 'POST':
        clients_form = ClientsForms(request.POST)

        if clients_form.is_valid():

            if not clients_form.cleaned_data['city']:
                messages.error(request, 'Selecione uma cidade')

            company_name = clients_form.cleaned_data.get('company_name', None)

            if company_name and Clients.objects.filter(company_name=company_name).exists():
                messages.error(request, 'Cliente já cadastrado')
            
            else:
                clients_form.save()
                messages.success(request, 'Novo cliente cadastrado!')
                return redirect('index')

    name = name_hello(request)
    return render(request, 'clients.html', {'clients_form': clients_form, 'name': name})


