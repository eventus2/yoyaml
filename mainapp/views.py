from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')

def products(request, pk=None):
   print(pk)
   links_menu = Category.objects.all()
   if pk:
       if pk == '0':
           products = Product.objects.all()
           category = {'name':'Все категории'}
       else:
           category = get_object_or_404(Category, pk=pk)
           products = Product.objects.filter(category__pk=pk)
       content = {
            'links_menu':links_menu,
            'category': category,
            'products': products
        }
       return render(request, 'catalog.html', content)
   products = Product.objects.all()

   content ={
       'links_menu': links_menu,
       'products': products,
        }

   return render(request, 'catalog.html', content)

def contacts(request):
    return render(request, 'contacts.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

