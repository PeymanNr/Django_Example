from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from basket.forms import AddToBasketForm
from catalogue.models import Product, Category
from catalogue.utils import check_is_active


def catalogue_list(request):
    return HttpResponse("Catalogue List Page")


def product(request):
    return HttpResponse("Product Page")


def post_detail(request, post_title):
    return HttpResponse(f"Post Detail {post_title}")


def archive_post(request, year):
    return HttpResponse(f"post Archive For Year {year}")

def product_list(request):
    context = dict()
    context['products'] = Product.objects.select_related('category').all()
    # context = "\n".join([f'{product.title}, {product.upc}, {product.category.name}' for product in products])
    # return HttpResponse(context)
    return render(request, 'catalogue/product_list.html', context=context)

def product_detail(request, pk):
    queryset = Product.objects.filter(is_active=True).filter(Q(pk=pk) | Q(upc=pk))
    if queryset.exists():
        product = queryset.first()
        form = AddToBasketForm({"product": product.id, "quantity": 1})
        return render(request, 'catalogue/product_detail.html', {"product":product, "form":form})
    raise Http404

def category_products(request, pk):
    try:
         category = Category.objects.prefetch_related('products').get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse("Category does not exist")
    products = category.products.all()
    context = "\n".join([f'{product.title}, {product.upc}' for product in products])
    return HttpResponse(context)

def product_search(request):
    title = request.GET.get('q')

    products = Product.objects.all().filter(title__icontains=title, is_active=True)
    context = "\n".join([f'{product.title}, {product.upc}' for product in products])
    return HttpResponse(f"Search page:\n{context}")

@login_required
@require_http_methods(request_method_list=['POST', 'GET'])
# @user_passes_test(check_is_active)
# @permission_required('has_score_permission')
def user_profile(request):
    return HttpResponse(f"hello {request.user.username}")
