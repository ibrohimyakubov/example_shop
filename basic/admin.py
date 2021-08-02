from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'count', 'price']
    search_fields = ['title']
    list_filter = ['category', 'status']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
