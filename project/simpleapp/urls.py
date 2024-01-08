from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate  #   create_product

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('<int:pk>', ProductDetail.as_view()),
    path('create/', ProductCreate.as_view(), name='product_create'),
    #path('create/', create_product, name='product_create')
]