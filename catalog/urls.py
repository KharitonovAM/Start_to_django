from django.urls import path
from .apps import CatalogConfig
from .views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contact/', contact)
]
