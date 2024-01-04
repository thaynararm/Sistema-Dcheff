from django.shortcuts import render, redirect
from django.contrib import messages
from apps.products.forms import ProductsForms, ProductsEntryForms
from apps.utilities.views import name_hello, check_athentication


#Visualização do cadastro de produtos
def product_registration(request):    
    #Verifica se o usuário está logado
    authentication_result = check_athentication(request)

    if authentication_result:
        return authentication_result

    #Exibe e instancia o formulário
    product_registration_form = ProductsForms() 

    if request.method == 'POST':
        product_registration_form = ProductsForms(request.POST)

        #Verifica se o formulário é valido e salva no banco de dados
        if product_registration_form.is_valid():
            product_registration_form.save()
            messages.success(request, 'Novo produto registrado!')
            return redirect('index')
        else:
             print(product_registration_form.errors)
             messages.error(request, 'Ocorreu um erro ao cadastrar o produto!')
             
                         
    name = name_hello(request)
    return render(request, 'products/product_registration.html', {'product_registration_form': product_registration_form, 'name': name})


#Visualização do registro de entradas de produtos
def product_entry(request):
    #Verifica se o usuário está logado
    authentication_result = check_athentication(request)

    if authentication_result:
        return authentication_result

    #Exibe e instancia o formulário
    products_entry_form = ProductsEntryForms() 

    if request.method == 'POST':
        products_entry_form = ProductsEntryForms(request.POST)

        #Verifica se o formulário é valido e salva no banco de dados
        if products_entry_form.is_valid():    
            products_entry_form.save()
            messages.success(request, 'Entrada de produto registrado!')
            return redirect('index')
                
        else:
             print(products_entry_form.errors)
             messages.error(request, 'Ocorreu um erro ao cadastrar a entrada!')
             
    
    name = name_hello(request)
    return render(request, 'products/product_entry.html', {'products_entry_form': products_entry_form,'name': name})