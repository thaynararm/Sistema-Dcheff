from django.contrib import admin
from apps.expenses.models import Expenses, RecipeSubcategoriesExpenses, RecipeCategoriesExpenses



class ListingExpenses(admin.ModelAdmin):
    list_display = ('description', 'date_of_competence', 'subcategory', 'source', 'value', 'delivery_date', 'receipt_account', 'receipt_status', 'comments', 'autor')
    list_display_links = ('description',)


class ListingSubcategoriesExpenses(admin.ModelAdmin):
    list_display = ('category_name', 'subcategory_name', 'autor')
    list_display_links = ('subcategory_name',)

class ListingCategoriesExpenses(admin.ModelAdmin):
    list_display = ('category_name', 'autor')
    list_display_links = ('category_name',)


admin.site.register(Expenses, ListingExpenses)
admin.site.register(RecipeSubcategoriesExpenses, ListingSubcategoriesExpenses)
admin.site.register(RecipeCategoriesExpenses, ListingCategoriesExpenses)

