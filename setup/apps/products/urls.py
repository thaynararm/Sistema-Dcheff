from django.urls import path
from apps.products.views import product_registration

urlpatterns = [
    path('product_registration/', product_registration, name='product_registration')
]
