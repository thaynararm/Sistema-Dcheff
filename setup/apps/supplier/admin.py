from django.contrib import admin
from apps.supplier.models import Supplier

class ListingSupplier(admin.ModelAdmin):
    list_display = ('company_name', 'seller_name', 'cnpj_cpf', 'contact','uf', 'city', 'address', 'email', 'observations')
    list_display_links = ('seller_name', 'cnpj_cpf')


admin.site.register(Supplier, ListingSupplier)
