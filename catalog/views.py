from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product
from .forms import ProductForm

class CatalogListView(ListView):
    model = Product


class CatalogDetailView(DetailView):
    model = Product


class CatalogCreateView(CreateView):
    model = Product
    form_class = ProductForm
    #fields = ("name", "description", "image", "category","price")
    success_url = reverse_lazy('catalog:index')


class CatalogUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

class CatalogDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
