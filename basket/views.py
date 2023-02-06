from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.decorators.http import require_POST

from basket.forms import AddToBasketForm
from basket.models import Basket
from catalogue.models import Product


# Create your views here.

@require_POST
def add_to_basket(request):
    response = HttpResponseRedirect(request.POST.get('next', '/'))
    basket =  Basket.get_basket(request.COOKIES.get('basket_id', None))
    if basket is None:
        raise Http404

    # product_id = request.POST.get('product_id', None)
    # if product_id is not None:
    #     try:
    #         product = Product.objects.get(pk=product_id)
    #     except Product.DoesNotExist:
    #         raise Http404
    #     else:
    #         basket.add(product)
    if not basket.validate_user(request.user):
        raise Http404

    form = AddToBasketForm(request.POST)
    if form.is_valid():
        form.save(basket)

    return response