from django.urls import path, re_path
from catalogue.views import product, catalogue_list, post_detail, archive_post, product_list, product_detail, category_products

urlpatterns = [
    path('list/', catalogue_list),
    path('product/', product),
    path('detail/<str:post_title>', post_detail),
    re_path(r"archive/(?P<year>[0-9]{2,4})/", archive_post),
    path('product/list/', product_list, name='product-list'),
    path('product/detail/<int:pk>/', product_detail, name='product-detail'),
    path('category/<int:pk>/products/', category_products, name='category-products')

]