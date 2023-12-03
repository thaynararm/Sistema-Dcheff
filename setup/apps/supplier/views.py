from django.shortcuts import render, redirect
from django.contrib import messages
from apps.supplier.models import Supplier
from apps.supplier.forms import SupplierForms
from apps.utilities.views import name_hello, check_athentication


def new_supplier(request):
    #Verifica se o usuário está logado
    authentication_result = check_athentication(request)

    if authentication_result:
        return authentication_result
    
    #Exibe e instancia o formulário
    supplier_form = SupplierForms()

    if request.method == 'POST':
        supplier_form = SupplierForms(request.POST)

        new_company_name = request.POST['company_name']

        #Verifica se o nome do cliente já está cadastrado
        if Supplier.objects.filter(company_name=new_company_name).exists():
            messages.error(request, 'Nome da empresa já cadastrado!')            

        
        #Verifica se o formulário é valido e salva no banco de dados
        if supplier_form.is_valid():
            try:
                supplier_form.save()
                messages.success(request, 'Novo fornecedor cadastrado!')
                return redirect('index')
            except:
                    messages.error(request, 'Ocorreu um erro ao cadastrar o cliente!')

    name = name_hello(request)
    return render(request, 'supplier.html', {'supplier_form': supplier_form, 'name': name})


