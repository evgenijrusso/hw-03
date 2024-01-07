from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter
from .models import Product, ProductMaterial, Material

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем, должен чем-то напомнить знакомые вам Django дженерики.

class ProductFilter(FilterSet):
    material = ModelMultipleChoiceFilter(
        field_name = 'productmaterial__material',
        queryset = Material.objects.all(),
        label = 'Material',
        conjoined = True,      #  Либо вместе and (True), либо по радельности (или) False
      #  empty_label = 'любой',
    )
    class Meta:
        # В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        model = Product
        # В fields мы описываем по каким полям модели  будет производиться фильтрация.
        fields = {
            # 'productmaterial__material': ['exact'],
            'name': ['icontains'],  # поиск по названию
            'quantity': ['gt'], # количество товаров должно быть больше или равно
            'price': [
                'lt',  # цена должна быть меньше или равна указанной
                'gt',  # цена должна быть больше или равна указанной
            ],
        }
