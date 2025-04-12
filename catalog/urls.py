from django.urls import path

from .apps import CatalogConfig
from .views import *

app_name = CatalogConfig.name

urlpatterns = [
    path("", list_products, name='index'),
    path("contact/", contact, name='contact'),
    path("base/", base_page, name='support'),
    path('products/<int:pk>/', products, name='select_product')

               ]
