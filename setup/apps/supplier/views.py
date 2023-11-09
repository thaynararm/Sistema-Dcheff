from django.shortcuts import render, redirect
from django.contrib import messages
from apps.supplier.forms import SupplierForms
from apps.index.views import name_hello

def new_supplier(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('index')

    form = SupplierForms()
    if request.method == 'POST':
        form = SupplierForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo fornecedor cadastrado!')
            return redirect('index')

    name = name_hello(request)
    return render(request, 'supplier.html', {'form': form, 'name': name})