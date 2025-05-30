from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


from .apps import CatalogConfig
from .views import CatalogListView, CatalogDetailView, CatalogCreateView, CatalogUpdateView, CatalogDeleteView

app_name = CatalogConfig.name


urlpatterns = [
    path("", CatalogListView.as_view(), name="index"),
    path("catalog/<int:pk>", CatalogDetailView.as_view(), name="catalog_detail"),
    path('catalog/', CatalogCreateView.as_view(), name='create_product'),
    path("contact/", TemplateView.as_view(template_name='catalog/contact.html'), name="contact"),
    path('catalog/<int:pk>/update', CatalogUpdateView.as_view(), name='catalog_update'),
    path('catalog/<int:pk>/delete', CatalogDeleteView.as_view(), name='catalog_delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)