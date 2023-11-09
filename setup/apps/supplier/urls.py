from django.urls import path
from apps.supplier.views import new_supplier

urlpatterns = [
    path('new_supplier/', new_supplier, name='new_supplier'),
]
