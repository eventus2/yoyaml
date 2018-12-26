from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import *
from mainapp.forms import FeedbackMessage
from basketapp.models import Basket


# Create your views here.
def getBasket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def index(request):
    basket = getBasket(request.user)
    content = {
        'products': products,
        'basket': basket,
    }
    return render(request, 'index.html', content)

def products(request, pk=None):
   basket = getBasket(request.user)
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
            'products': products,
            'basket': basket,
        }
       return render(request, 'catalog.html', content)
   products = Product.objects.all()

   content ={
       'links_menu': links_menu,
       'products': products,
       'basket':basket,
        }

   return render(request, 'catalog.html', content)

def contacts(request):
    basket = getBasket(request.user)
    if request.method == 'POST':
        form = FeedbackMessage(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form =FeedbackMessage()

    return render(request, 'contacts.html', {'form':form, 'basket':basket})

def product_detail(request, pk):
    basket = getBasket(request.user)
    product = get_object_or_404(Product, pk=pk)
    content = {
        'product': product,
        'basket' : basket,
    }
    return render(request, 'product_detail.html', content)

