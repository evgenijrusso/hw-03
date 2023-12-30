from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Product


class ProductList(ListView):
    model = Product    # Указываем модель, объекты которой мы будем выводить
    ordering = 'name'  # Поле, которое будет использоваться для сортировки объектов
    template_name = 'products.html'  # Указываем имя шаблона
    context_object_name = 'products' # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.


