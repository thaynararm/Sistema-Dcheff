from django.urls import path
from apps.clients.views import new_client, previous_page

urlpatterns = [
    path('new_client/', new_client, name='new_client'),
    path('redirect/', previous_page, name='previous_page'),
]
