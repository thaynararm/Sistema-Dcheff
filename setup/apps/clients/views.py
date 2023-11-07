from django.shortcuts import render, redirect
from django.contrib import messages
from apps.clients.forms import ClientsForms
from apps.index.views import name_hello

def new_client(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('clients')

    form = ClientsForms
    if request.method == 'POST':
        form = ClientsForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo cliente cadastrado!')
            return redirect('index')

    name = name_hello(request)
    return render(request, 'clients/clients.html', {'form': form, 'name': name})

def previous_page(request):
    previous_page = request.META.get('HTTP_REFERER')
    if previous_page:
        return redirect(previous_page)
    else:
        return redirect('index.html')