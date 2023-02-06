from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic import ListView, FormView

from shipping.forms import ShippingAddressForm
from shipping.models import ShippingAddress


# Create your views here.;

#
#
# @login_required
# @require_http_methods(request_method_list=['POST', 'GET'])
# def address_create(request):
#     if request.method == 'POST':
#         form = ShippingAddressForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.user = request.user
#             instance.save()
#             return redirect('address-list')
#
#     else:
#        form = ShippingAddressForm()
#     return render(request, 'shipping/create.html', {'form':form})
#
# @login_required()
# @require_GET
# def address_list(request):
#     queryset = ShippingAddress.objects.filter(user=request.user)
#
#     return render(request, 'shipping/list.html', {'queryset':queryset})

class CustomUserView(ListView):
    # model = ShippingAddress
    # template_name = 'shipping/list.html'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs =super().get_queryset()
        return qs.filter(user=self.request.user)


class AddressListView(CustomUserView):
    model = ShippingAddress
    template_name = 'shipping/list.html'

class AddressCreateView(FormView):
    form_class = ShippingAddressForm
    template_name = 'shipping/create.html'
    # success_url = '/shipping/list/'
    success_url = reverse_lazy('address-list')

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = self.request.user
            instance.save()
            return super().form_valid(form)
