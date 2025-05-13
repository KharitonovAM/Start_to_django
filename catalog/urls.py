from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .apps import CatalogConfig
from .views import CatalogListView

app_name = CatalogConfig.name


urlpatterns = [
    path("", CatalogListView.as_view(), name="index"),

]


# urlpatterns = [
#     path("", list_products, name="index"),
#     path("contact/", contact, name="contact"),
#     path("base/", base_page, name="support"),
#     path("products/<int:pk>/", products, name="select_product"),
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)