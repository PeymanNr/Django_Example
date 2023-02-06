from django.contrib import admin
from django.contrib.admin import register
from basket.models import BasketLine, Basket


# Register your models here.

class BasketLineAdmin(admin.TabularInline):
    model = BasketLine

@register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_time']
    inlines = [BasketLineAdmin,]