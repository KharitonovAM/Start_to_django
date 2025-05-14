from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .apps import CatalogConfig
from .views import CatalogListView, CatalogDetailView, CatalogCreateView, ContactListView

app_name = CatalogConfig.name


urlpatterns = [
    path("", CatalogListView.as_view(), name="index"),
    path("catalog/<int:pk>", CatalogDetailView.as_view(), name="catalog_detail"),
    path('catalog/', CatalogCreateView.as_view(), name='create_product'),
    path("contact/", ContactListView.as_view(), name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)