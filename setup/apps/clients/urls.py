from django.urls import path
from apps.clients.views import new_client

urlpatterns = [
    path('new_client/', new_client, name='new_client')
]
