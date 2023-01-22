from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.


#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'category_name', 'unit_price')
    search_fields = ('name_product', 'description')
    list_filter = ('category_name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    search_fields = ('category_name',)
    list_filter = ('category_name',)