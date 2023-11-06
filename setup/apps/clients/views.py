from django.shortcuts import render, redirect
from apps.clients.forms import ClientsForms
from apps.index.views import name_hello

def clients(request):
    
    if request.method == 'POST':
        form = ClientsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
    else:
        form = ClientsForms()

    name = name_hello(request)    
    return render(request, 'clients/clients.html', {'form': form, 'name': name})
