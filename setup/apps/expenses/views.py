from django.shortcuts import render, redirect
from django.contrib import messages
from apps.expenses.forms import ExpensesForms
from apps.utilities.views import name_hello, check_athentication



def new_expense(request):    
    #Verifica se o usuário está logado
    authentication_result = check_athentication(request)

    if authentication_result:
        return authentication_result

    #Exibe e instancia o formulário
    expenses_form = ExpensesForms() 

    if request.method == 'POST':
        expenses_form = ExpensesForms(request.POST)

        #Verifica se o formulário é valido e salva no banco de dados
        if expenses_form.is_valid():
                try:
                    expenses_form.save()
                    messages.success(request, 'Nova despesa registrada!')
                    return redirect('index')
                except:
                    messages.error(request, 'Ocorreu um erro ao cadastrar a despesa!')

        else:
             messages.error(request, 'Ocorreu um erro ao cadastrar a despesa!')
             print(expenses_form.errors)
                         
    name = name_hello(request)
    return render(request, 'new_expense.html', {'expenses_form': expenses_form, 'name': name})


