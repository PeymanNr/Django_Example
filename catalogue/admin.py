from django.contrib import admin
from django.contrib.admin import register

from catalogue.models import Category, Brand ,Product, ProductType, ProductAttribute

# Register your models here.

class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1

@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['upc', 'product_type', 'is_active', 'title', 'category', 'brand']
    list_filter = ['is_active']
    list_display_links = ['upc']
    search_fields = ['upc', 'title', 'category__name']
    list_editable = ['is_active']
    actions = ['active_all']

    def active_all(self, request, queryset):
        pass

    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_view_permission(self, request, obj=None):
    #     return False


@register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_type', 'attribute_type']

@register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ProductAttributeInline]


admin.site.register(Category)
admin.site.register(Brand)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductType)