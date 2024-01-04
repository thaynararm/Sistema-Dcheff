from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from apps.supplier.models import Supplier


class RecipeCategoriesProducts(models.Model):
    category_name = models.CharField(max_length=100, blank=False, null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.category_name
    

class RecipeSubcategoriesProducts(models.Model):
    category_name = models.ForeignKey(RecipeCategoriesProducts, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100, blank=False, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.subcategory_name
    

class UnitOfMeasurement(models.Model):
    unit_of_measurement = models.CharField(max_length=100, blank=False, null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.unit_of_measurement


class Products(models.Model):
    product_name = models.CharField(max_length=100, blank=False, null=False)
    product_code = models.CharField(max_length=50, blank=False, null=False, unique=True)
    subcategory = models.ForeignKey(RecipeSubcategoriesProducts, on_delete=models.SET_DEFAULT, default=1)
    unit_of_measurement = models.ForeignKey(UnitOfMeasurement, on_delete=models.SET_DEFAULT, default=1)
    quantity_in_stock = models.CharField(max_length=100, blank=False, null=False)
    sale_value = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)
    location_in_stock = models.CharField(max_length=100, blank=True, null=True)
    availability = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='products_autor')


    def __str__(self):
        return self.product_name


class EntryProductsForms(models.Model):
    product_name = models.ForeignKey(Products, on_delete=models.SET_DEFAULT, default=1)
    unit_of_measurement = models.ForeignKey(UnitOfMeasurement, on_delete=models.SET_DEFAULT, default=1)
    quantity = models.CharField(max_length=100, blank=False, null=False)
    unitary_value = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)
    total_value = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)
    entry_date = models.DateField(default=datetime.now, blank=False, null=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_DEFAULT, default=1)
    invoice_number = models.CharField(max_length=100, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='products_entry_autor')


