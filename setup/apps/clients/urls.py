from django.urls import path
from apps.clients.views import clients

urlpatterns = [
    path('clients', clients, name='clients')
]
