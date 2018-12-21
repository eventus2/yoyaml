"""yoyaml_lesson1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path
import mainapp.views as mainapp
# import authapp.views as authapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.index, name='index'),
    path('products/', mainapp.products, name='products'),
    path('contacts/', mainapp.contacts, name="contacts"),
    path('hello_baby/', mainapp.hello_baby, name="hello_baby"),
    path('teknum/', mainapp.teknum, name="teknum"),
    path('yoya_kingmoon/', mainapp.yoya_kingmoon, name='yoya_kingmoon'),
    path('hello_baby_big/', mainapp.hello_baby_big, name='hello_baby_big'),
    path('teknum_big/', mainapp.teknum_big, name ='teknum_big'),
    path('yoya_kingmoon_big/', mainapp.yoya_kingmoon_big, name='yoya_kingmoon_big'),
    path('product_detail/<int:pk>/', mainapp.product_detail, name='product_detail')
    # path('login/',authapp.login, name='login'),
    # path('logout/', authapp.logout, name='logout'),
    # path('register/', authapp.register, name='register'),
    # path('edit/', authapp.edit, name='edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)