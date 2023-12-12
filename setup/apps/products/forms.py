from django import forms
from datetime import datetime
from apps.products.models import Products, EntryProductsForms


#Cadastro de Produtos
class ProductsForms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductsForms, self).__init__(*args, **kwargs)
        # Defina a data atual como valor inicial para o campo date_of_competence
        self.fields['sale_value'].localize = True
        self.fields['sale_value'].widget.is_localized = True
    

    class Meta:
        model = Products        #Especifica quais campos do modelo devem ser incluídos no formulário

        #Especifica quais campos do modelo devem ser incluídos no formulário        
        fields = ['product_name', 'product_code', 'subcategory', 'unit_of_measurement', 'quantity_in_stock', 'sale_value', 'location_in_stock', 'availability', 'comments']
            
        #Define os rótulos dos campos
        labels = {
            'product_name': 'Nome do Produto',
            'product_code': 'Código do Produto',
            'subcategory': 'Categoria',
            'unit_of_measurement': 'Unidade de Medida',
            'quantity_in_stock': 'Quantidade em Estoque',
            'sale_value': 'Valor de Venda',
            'location_in_stock': 'Localização no Estoque',
            'availability': 'Disponibilidade',
            'comments': 'Descrições adicionais do produto',
        }

        #Define como cada campo deve ser exibido
        widgets = {
            'product_name': forms.TextInput(attrs={
                'placeholder': 'Nome do Produto',}),
            'product_code': forms.TextInput(attrs={
                'placeholder': 'Código do Produto',}),            
            'subcategory': forms.Select(attrs={
                'id': 'subcategory'}),
            'unit_of_measurement': forms.Select(attrs={
                'id': 'source',
                'class': 'combobox'}),
            'quantity_in_stock': forms.TextInput(attrs={
                'placeholder': 'Quantidade',}),
            'sale_value': forms.TextInput(attrs={
                'placeholder': '0,00',
                'id': 'value',
                'step':'0.01',
                'localize': 'True'}),
            'location_in_stock': forms.TextInput(attrs={
                'placeholder': 'Local de Armazenamento'}),
            'availability': forms.CheckboxInput(attrs={
                'type': 'checkbox',
            }),
            'comments': forms.TextInput(attrs={
                'placeholder': 'Observações',}),
            }
        
        
class ProductsEntryForms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductsEntryForms, self).__init__(*args, **kwargs)
        self.fields['unitary_value'].localize = True
        self.fields['unitary_value'].widget.is_localized = True
        self.fields['total_value'].localize = True
        self.fields['total_value'].widget.is_localized = True
        self.fields['entry_date'].initial = datetime.today().strftime('%Y-%m-%d')
        
    
    class Meta:
        model = EntryProductsForms        #Especifica quais campos do modelo devem ser incluídos no formulário

        #Especifica quais campos do modelo devem ser incluídos no formulário        
        fields = ['product_name', 'unit_of_measurement', 'quantity', 'unitary_value', 'total_value', 'entry_date', 'supplier', 'invoice_number', 'comments']
            
        #Define os rótulos dos campos
        labels = {
            'product_name': 'Nome do Produto',
            'unit_of_measurement': 'Unidade de Medida',
            'quantity': 'Quantidade',
            'unitary_value': 'Valor Unitário de Compra',
            'total_value': 'Valor Total da Compra',
            'entry_date': 'Data de Entrada',
            'supplier': 'Fornecedor',
            'invoice_number': 'Nota Fiscal',
            'comments': 'Descrições Adicionais da Entrada'
        }

        #Define como cada campo deve ser exibido
        widgets = {
            'product_name': forms.Select(attrs={}),
            'unit_of_measurement': forms.Select(attrs={
                'id': 'source',
                'class': 'combobox'}),
            'quantity': forms.TextInput(attrs={
                'placeholder': 'Quantidade',}),
            'unitary_value': forms.TextInput(attrs={
                'placeholder': '0,00',
                'class': 'value',
                'step':'0.01',
                'localize': 'True'}),
            'total_value': forms.TextInput(attrs={
                'placeholder': '0,00',
                'class': 'value',
                'step':'0.01',
                'localize': 'True'}),    
            'entry_date': forms.TextInput(
                attrs={
                'class': 'date'}),        
            'supplier': forms.Select(attrs={}),
            'invoice_number': forms.TextInput(attrs={
                'placeholder': 'Código da Nota Fiscal',
            }),
            'comments': forms.TextInput(attrs={
                'placeholder': 'Observações',}),
            }
        
