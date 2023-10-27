from django import forms
from apps.clients.models import Clients

class ClientsForms(forms.ModelForm):
    class Meta:
        model = Clients

        #Especifica quais campos do modelo devem ser incluídos no formulário
        fields = ['company_name', 'responsible_name', 'cnpj_cpf', 'contact', 'city']
            
        #Define os rótulos dos campos
        labels = { 
            'company_name': 'Nome da empresa:',
            'responsible_name': 'Nome do Responsável pela Empresa:',
            'cnpj_cpf': 'CNPJ ou CPF:',
            'contact': 'Número de Contato:',
            'city': 'Cidade',
        }

        #Define como cada campo deve ser exibido
        widgets = {
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Digite o nome da empresa',
                'class': 'form-items'}),
            'responsible_name': forms.TextInput(attrs={
                'placeholder': 'Digite o nome do responsável pela empresa',
                 'class': 'form-items'}),
            'cnpj_cpf': forms.TextInput(attrs={
                'placeholder': 'Digite o CNPJ da empresa ou CPF do responsável',
                'class': 'form-items'}),
            'contact': forms.TextInput(attrs={
                'placeholder': '(xx) xxxxx-xxxx',
                'class': 'form-items'}),
            'city': forms.Select(attrs={
                'class': 'form-items'}),
        }

        