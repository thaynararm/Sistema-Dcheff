from django.urls import path
from apps.products.views import product_registration, product_entry

urlpatterns = [
    path('product_registration/', product_registration, name='product_registration'),
    path('product_entry/', product_entry, name='product_entry'),
]
