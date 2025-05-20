from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Product


class CatalogListView(ListView):
    model = Product

class CatalogDetailView(DetailView):
    model = Product


class CatalogCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image", "category","price")
    success_url = reverse_lazy('catalog:index')


class CatalogUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy('catalog:index')
