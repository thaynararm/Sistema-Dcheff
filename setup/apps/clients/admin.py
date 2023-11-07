from django.contrib import admin
from apps.clients.models import Clients, City


class ListingClients(admin.ModelAdmin):
    list_display = ('company_name', 'responsible_name', 'cnpj_cpf', 'contact', 'city', 'address', 'email', 'observations')
    list_display_links = ('company_name', 'cnpj_cpf')

class ListingCity(admin.ModelAdmin):
    list_display = ('name_city', 'uf_city',)
    list_display_links = ('name_city', 'uf_city',)

admin.site.register(Clients, ListingClients)
admin.site.register(City, ListingCity)

