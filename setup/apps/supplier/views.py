from django.shortcuts import render, redirect
from django.contrib import messages
from apps.supplier.models import Supplier
from apps.supplier.forms import SupplierForms
from apps.index.views import name_hello


def new_supplier(request):
    #Verifica se o usuário está logado
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('index')

    supplier_form = SupplierForms()

    if request.method == 'POST':
        supplier_form = SupplierForms(request.POST)

        if supplier_form.is_valid():

            if not supplier_form.cleaned_data['city']:
                messages.error(request, 'Selecione uma cidade')

            company_name = supplier_form.cleaned_data.get('company_name', None)

            if company_name and Supplier.objects.filter(company_name=company_name).exists():
                messages.error(request, 'Fornecedor já cadastrado')
            
            else:
                supplier_form.save()
                messages.success(request, 'Novo fornecedor cadastrado!')
                return redirect('index')

    name = name_hello(request)
    return render(request, 'supplier.html', {'supplier_form': supplier_form, 'name': name})


