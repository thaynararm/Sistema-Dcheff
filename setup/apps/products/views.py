from django.shortcuts import render, redirect
from django.contrib import messages
from apps.products.forms import ProductsForms
from apps.utilities.views import name_hello, check_athentication



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
                try:
                    product_registration_form.save()
                    messages.success(request, 'Novo produto registrado!')
                    return redirect('index')
                except:
                    messages.error(request, 'Ocorreu um erro ao cadastrar o produto!')

        else:
             messages.error(request, 'Ocorreu um erro ao cadastrar o produto!')
             print(product_registration_form.errors)
                         
    name = name_hello(request)
    return render(request, 'product_registration.html', {'product_registration_form': product_registration_form, 'name': name})


