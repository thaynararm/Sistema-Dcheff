from django.contrib import admin
from apps.revenues.models import Revenues, RecipeSubcategories, RecipeCategories



class ListingRevenues(admin.ModelAdmin):
    list_display = ('description', 'date_of_competence', 'subcategory', 'source', 'value', 'delivery_date', 'receipt_account', 'receipt_status', 'comments')
    list_display_links = ('description',)


class ListingSubcatergories(admin.ModelAdmin):
    list_display = ('category_name', 'subcategory_name')
    list_display_links = ('subcategory_name',)

class ListingCatergories(admin.ModelAdmin):
    list_display = ('category_name',)
    list_display_links = ('category_name',)


admin.site.register(Revenues, ListingRevenues)
admin.site.register(RecipeSubcategories, ListingSubcatergories)
admin.site.register(RecipeCategories, ListingCatergories)

