from catalogue.models import Category
from django import template

register = template.Library()
@register.simple_tag()
def get_category():
    return Category.objects.all()