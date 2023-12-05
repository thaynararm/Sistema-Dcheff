from django.urls import path
from apps.expenses.views import new_expense

urlpatterns = [
    path('new_expense/', new_expense, name='new_expense')
]
