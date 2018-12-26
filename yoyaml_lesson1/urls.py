from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp
# import authapp.views as authapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.index, name='index'),
    path('products/<int:pk>/', mainapp.products, name='products'),
    path('contacts/', mainapp.contacts, name="contacts"),
    path('product_detail/<int:pk>/', mainapp.product_detail, name='product_detail'),
    path('auth/', include ('authapp.urls', namespace='auth')),
    path('basket', include ('basketapp.urls', namespace='basket')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)