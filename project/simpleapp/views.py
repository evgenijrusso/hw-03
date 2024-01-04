from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class ProductList(ListView):
    model = Product    # Указываем модель, объекты которой мы будем выводить
    ordering = 'name'  # Поле, которое будет использоваться для сортировки объектов
    #queryset = Product.objects.filter(price__lt=120).order_by('name')
    template_name = 'products.html'  # Указываем имя шаблона
    context_object_name = 'products' # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.


    # Метод get_context_data позволяет нам изменить набор данных,  который будет передан в шаблон.
    # С помощью super() мы обращаемся к родительским классам и вызываем у них метод get_context_data
    # с теми же аргументами,  что и были переданы нам.  В ответе мы должны получить словарь.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # К словарю добавим текущую дату в ключ 'time_now'.
        # Добавим ещё одну пустую переменную, чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        pprint(context)
        return context

class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Product
    # Используем другой шаблон — product.html
    template_name = 'product.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'product'