from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.core.cache import cache


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)],)
    # поле категории будет ссылаться на модель категории
    # все продукты в категории будут доступны через поле products
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(validators=[MinValueValidator(0.0)],)

    # допишем свойство, которое будет отображать, есть ли товар на складе
    @property
    def on_stock(self):
        return self.quantity > 0

    def __str__(self):
        return f'{self.name} {self.quantity}'

    def get_absolute_url(self): # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return reverse('product_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'product-{self.pk}')
        # затем удаляем его из кэша, чтобы сбросить его


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # Категория, к которой будет привязываться товар

    def __str__(self):
        return f'{self.name}'

# --------------------------------------------------


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

