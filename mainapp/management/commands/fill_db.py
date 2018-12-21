from django.core.management.base import BaseCommand
from mainapp.models import Category, Product
from django.contrib.auth.models import User

import json, os

JSON_PATH = 'mainapp/json'

def loadFromJSON (file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command (BaseCommand):
    print('Запуск скрипта')


    def handle(self, *args, **options):
        categories = loadFromJSON ('categories')

        Category.objects.all().delete()
        for category in categories:
            new_category = Category(**category)
            new_category.save()

        Product.object.all().delete()
        for product in products:
            category_name = product["category"]
            _category = Categiry.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new.product.save()

        User.objects.all().delete()
