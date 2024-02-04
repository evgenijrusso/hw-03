from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate, \
    ProductUpdate, ProductDelete  #   create_product

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    #path('create/', create_product, name='product_create')
]