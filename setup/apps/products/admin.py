from django.contrib import admin
from apps.products.models import Products, RecipeCategoriesProducts, RecipeSubcategoriesProducts, UnitOfMeasurement



class ListingProducts(admin.ModelAdmin):
    list_display = ('product_name', 'product_code', 'subcategory', 'unit_of_measurement', 'quantity_in_stock', 'sale_value', 'location_in_stock', 'availability', 'comments')
    list_display_links = ('product_name',)


class ListingSubcategoriesProducts(admin.ModelAdmin):
    list_display = ('category_name', 'subcategory_name', 'autor')
    list_display_links = ('subcategory_name',)


class ListingCategoriesProducts(admin.ModelAdmin):
    list_display = ('category_name', 'autor')
    list_display_links = ('category_name',)


class ListingUnitOfMeasurement(admin.ModelAdmin):
    list_display = ('unit_of_measurement', 'autor')
    list_display_links = ('unit_of_measurement',)

admin.site.register(Products, ListingProducts)
admin.site.register(RecipeSubcategoriesProducts, ListingSubcategoriesProducts)
admin.site.register(RecipeCategoriesProducts, ListingCategoriesProducts)
admin.site.register(UnitOfMeasurement, ListingUnitOfMeasurement)
