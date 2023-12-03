from django import forms
from apps.clients.models import Clients


class ClientsForms(forms.ModelForm):
    class Meta:
        model = Clients        #Especifica quais campos do modelo devem ser incluídos no formulário

        #Especifica quais campos do modelo devem ser incluídos no formulário        
        fields = ['company_name', 'cnpj_cpf', 'responsible_name', 'uf', 'city', 'contact', 'address', 'email', 'observations']
            
        #Define os rótulos dos campos
        labels = { 
            'company_name': 'Nome da empresa',
            'cnpj_cpf': 'CNPJ ou CPF',
            'responsible_name': 'Nome do Responsável pela Empresa',
            'contact': 'Número de Contato',
            'uf': 'Estado',
            'city': 'Cidade',
            'address': 'Endereço do Cliente',
            'email': 'Email',
            'observations': 'Observações',
            }

        #Define como cada campo deve ser exibido
        widgets = {
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Digite o nome da empresa',}),
            'cnpj_cpf': forms.TextInput(attrs={
                'placeholder': 'Digite o CNPJ da empresa ou CPF do responsável',}),
            'responsible_name': forms.TextInput(attrs={
                'placeholder': 'Digite o nome do responsável pela empresa',}),
            'contact': forms.TextInput(attrs={
                'placeholder': '(xx) xxxxx-xxxx',}),
            'uf': forms.Select(attrs={
                'class': 'state-field',
                'id': 'uf'}),
            'city': forms.Select(attrs={
                'class': 'city-field',
                'id': 'city'}),
            'address': forms.TextInput(attrs={
                'placeholder': 'Digite o endereço da empresa ou do responsável',}),
            'email': forms.EmailInput(attrs={
                'placeholder': 'exemplo@email.com',}),
            'observations': forms.TextInput(attrs={
                'placeholder': 'Observações',}),
        }
    