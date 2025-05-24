from django.urls import path
from django.views.generic import TemplateView

from .views import *
urlpatterns = [path("blog/", TemplateView.as_view(template_name='blog/base.html'), name="blog"),
               ]