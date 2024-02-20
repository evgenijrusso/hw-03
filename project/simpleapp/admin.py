from django.contrib import admin
from .models import Category, Product, Material, ProductMaterial

# list_display — это список или кортеж со всеми полями, которые Вы хотите видеть в таблице с товарами

# все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий
# информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
def nullfy_quantity(ModelAdmin, request, queryset):
    queryset.update(quantity=0)

nullfy_quantity.short_description = 'Обнулить товары'
# описание для более понятного представления в админ панеле задаётся, как будто это объект


class ProductAdmin(admin.ModelAdmin):  # создаём новый класс для представления товаров в админке
   #  list_display = [field.name for field in Product._meta.get_fields()]

    list_display = ('name', 'description', 'quantity', 'price', 'on_stock')
    list_filter = ('price', 'quantity', 'name')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('name', 'category__name')  # тут всё очень похоже на фильтры из запросов в базу
    actions = [nullfy_quantity]  # добавляем действия в список


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Material)
admin.site.register(ProductMaterial)
