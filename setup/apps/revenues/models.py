from django.db import models
from apps.clients.models import Clients
from datetime import datetime


class RecipeCategories(models.Model):
    category_name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.category_name

class RecipeSubcategories(models.Model):
    category_name = models.ForeignKey(RecipeCategories, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100, blank=False, null=True)

    def __str__(self):
        return self.subcategory_name


class Revenues(models.Model):
    description = models.CharField(max_length=100, blank=False, null=False)
    date_of_competence = models.DateField(default=datetime.now, blank=False, null=False)
    subcategory = models.ForeignKey(RecipeSubcategories, on_delete=models.SET_DEFAULT, default='Receita a Identificar')
    source = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True)
    value = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)
    delivery_date = models.DateField(default=datetime.now, blank=False, null=False)
    receipt_account = models.CharField(max_length=100)
    receipt_status = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description
    