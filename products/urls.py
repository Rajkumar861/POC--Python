from django.urls import path,include
from .views import welcome_note,product_list,update_product
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',welcome_note,name='welcome'),
    path('product/',product_list,name='products'),
    path('product/<int:id>/',update_product,name='update'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)