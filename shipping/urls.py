from django.urls import path

from shipping.views import AddressListView, AddressCreateView

urlpatterns = [
    path('create/', AddressCreateView.as_view(), name='address-create'),
    path('list/', AddressListView.as_view(), name='address-list')
]