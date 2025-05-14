from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View

from .models import Product


class CatalogListView(ListView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class CatalogDetailView(DetailView):
    model = Product

class CatalogCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image", "category","price")
    success_url = reverse_lazy('catalog:index')
