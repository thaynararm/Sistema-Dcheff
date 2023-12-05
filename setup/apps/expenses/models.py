from django.db import models
from apps.supplier.models import Supplier
from datetime import datetime
from django.contrib.auth.models import User


class RecipeCategoriesExpenses(models.Model):
    category_name = models.CharField(max_length=100, blank=False, null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.category_name

class RecipeSubcategoriesExpenses(models.Model):
    category_name = models.ForeignKey(RecipeCategoriesExpenses, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100, blank=False, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.subcategory_name


class Expenses(models.Model):
    description = models.CharField(max_length=100, blank=False, null=False)
    date_of_competence = models.DateField(default=datetime.now, blank=False, null=False)
    subcategory = models.ForeignKey(RecipeSubcategoriesExpenses, on_delete=models.SET_DEFAULT, default=1)
    source = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, related_name='expenses_source')
    value = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)
    delivery_date = models.DateField(default=datetime.now, blank=False, null=False)
    receipt_account = models.CharField(max_length=100)
    receipt_status = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='expenses_autor')
    
    def save(self, *args, **kwargs):
        self.value = abs(self.value) * -1
        super().save(*args, **kwargs)

    
    def __str__(self):
        return f'{self.description} - R${self.value}'
    