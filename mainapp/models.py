from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Наименование товара')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Наименование категории')
    color = models.CharField(max_length = 15, verbose_name='Цвет')
    short_decription = models.CharField(max_length=30, verbose_name='Краткое описание товара', null=True)
    description = models.TextField()
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе')
    price = models.DecimalField(verbose_name='Цена товара', max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to = 'products', null=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    client_name = models.CharField(max_length=32, verbose_name='Имя')
    email = models.EmailField(max_length=254, blank=True, verbose_name=' E-mail')
    topic = models.CharField(max_length=32,verbose_name='Тема сообщения')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.topic