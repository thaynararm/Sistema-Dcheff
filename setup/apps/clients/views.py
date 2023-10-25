from django.shortcuts import render, redirect
from apps.clients.forms import ClientsForms

def clients(request):
    if request.method == 'POST':
        form = ClientsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
    else:
        form = ClientsForms()
    
    return render(request, 'clients/clients.html', {'form': form})
