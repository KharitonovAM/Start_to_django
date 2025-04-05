from django.urls import path

from .apps import CatalogConfig
from .views import contact, home

app_name = CatalogConfig.name

urlpatterns = [path("", home), path("contact/", contact)]
