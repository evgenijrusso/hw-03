from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from datetime import datetime
from .models import Product
from .filters import ProductFilter
from .forms import ProductForm
from django.http import HttpResponse, HttpResponseRedirect


class ProductList(ListView):
    model = Product    # Указываем модель, объекты которой мы будем выводить
    ordering = 'name'  # Поле, которое будет использоваться для сортировки объектов
    template_name = 'products.html'  # Указываем имя шаблона
    context_object_name = 'products' # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    paginate_by = 2  # вот так мы можем указать количество записей на странице

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = ProductFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs


    # Метод get_context_data позволяет нам изменить набор данных,  который будет передан в шаблон.
    # С помощью super() мы обращаемся к родительским классам и вызываем у них метод get_context_data
    # с теми же аргументами,  что и были переданы нам.  В ответе мы должны получить словарь.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # К словарю добавим текущую дату в ключ 'time_now'.
        # Добавим ещё одну пустую переменную, чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        context['filterset'] = self.filterset
        return context

class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Product
    # Используем другой шаблон — product.html
    template_name = 'product.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'product'

class ProductCreate(CreateView):
    form_class = ProductForm # Указываем нашу разработанную форму
    model = Product # модель товаров
    template_name = 'product_edit.html'


# Добавляем представление для изменения товара.
class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


# Представление удаляющее товар.
class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')


#
# def create_product(request):
#     form = ProductForm(request.GET)  # перенес выше, чтобы видет возможные ошибки при  невалидности формы
#
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/products/')
#
#     return render(request, 'product_edit.html', {'form': form})
