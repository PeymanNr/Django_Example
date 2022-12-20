from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from catalogue.models import Product, Category


# Create your views here.


def catalogue_list(request):
    return HttpResponse("Catalogue List Page")


def product(request):
    return HttpResponse("Product Page")


def post_detail(request, post_title):
    return HttpResponse(f"Post Detail {post_title}")


def archive_post(request, year):
    return HttpResponse(f"post Archive For Year {year}")

def product_list(request):
    products = Product.objects.select_related('category').all()
    context = "\n".join([f'{product.title}, {product.upc}, {product.category.name}' for product in products])
    return HttpResponse(context)

def product_detail(request, pk):
    # product = Product.objects.get(pk=pk)
    # return HttpResponse(f"title: {product.title}")
    queryset = Product.objects.filter(is_active=True).filter(Q(pk=pk) | Q(upc=pk))
    if queryset.exists():
        product = queryset.first()
        return HttpResponse(f"title: {product.title}")
    return HttpResponse("Products does not exist")

def category_products(request, pk):
    try:
         category = Category.objects.prefetch_related('products').get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse("Category does not exist")
    products = category.products.all()
    context = "\n".join([f'{product.title}, {product.upc}' for product in products])
    return HttpResponse(context)