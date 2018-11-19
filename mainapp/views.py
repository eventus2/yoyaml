from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def catalog(request):
    return render(request, 'catalog.html')

def contacts(request):
    return render(request, 'contacts.html')

def hello_baby(request):
    return render(request, 'hello_baby.html')

def teknum(request):
    return render(request, 'teknum.html')

def yoya_kingmoon(request):
    return render(request, 'yoya_kingmoon.html')

def hello_baby_big(request):
    return render(request, 'hello_baby_big.html')

def teknum_big(request):
    return render(request, 'teknum_big.html')

def yoya_kingmoon_big(request):
    return render(request, 'yoya_kingmoon_big.html')