from django import forms
from apps.supplier.models import Supplier

class SupplierForms(forms.ModelForm):
    class Meta:
        model = Supplier

        #Especifica quais campos do modelo devem ser incluídos no formulário
        fields = ['company_name', 'cnpj_cpf', 'seller_name', 'contact', 'city', 'address', 'email', 'observations']
            
        #Define os rótulos dos campos
        labels = { 
            'company_name': 'Nome da empresa',
            'cnpj_cpf': 'CNPJ ou CPF',
            'seller_name': 'Nome do Vendedor da Empresa',
            'contact': 'Número de Contato',
            'city': 'Cidade',
            'address': 'Endereço do Cliente',
            'email': 'Email',
            'observations': 'Observações'
        }

        #Define como cada campo deve ser exibido
        widgets = {
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Digite o nome da empresa',}),
            'cnpj_cpf': forms.TextInput(attrs={
                'placeholder': 'Digite o CNPJ da empresa ou CPF do responsável',}),
            'seller_name': forms.TextInput(attrs={
                'placeholder': 'Digite o nome do responsável pela empresa',}),
            'contact': forms.TextInput(attrs={
                'placeholder': '(xx) xxxxx-xxxx',}),
            'city': forms.Select(attrs={}),
            'address': forms.TextInput(attrs={
                'placeholder': 'Digite o endereço da empresa ou do responsável',}),
            'email': forms.TextInput(attrs={
                'placeholder': 'exemplo@email.com',}),
            'observations': forms.TextInput(attrs={
                'placeholder': 'Observações',}),
        }

        