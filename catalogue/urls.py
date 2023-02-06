from django.urls import path, re_path
from catalogue.views import product, catalogue_list, post_detail, archive_post, product_list, product_detail, \
    category_products, product_search, user_profile

urlpatterns = [
    path('list/', catalogue_list),
    path('product/', product),
    path('detail/<str:post_title>', post_detail),
    re_path(r"archive/(?P<year>[0-9]{2,4})/", archive_post),
    path('product/list/', product_list, name='product-list'),
    path('product/detail/<int:pk>/', product_detail, name='product-detail'),
    path('product/search/', product_search, name='product-search'),
    path('category/<int:pk>/products/', category_products, name='category-detail'),
    path('profile/', user_profile, name='user-profile')


]