from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import ProductForm
from .models import Product


class CatalogListView(ListView):
    model = Product


class CatalogDetailView(DetailView):
    model = Product


class CatalogCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    # fields = ("name", "description", "image", "category","price")
    success_url = reverse_lazy("catalog:index")
    login_url = reverse_lazy("users:register")


class CatalogUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:index")
    login_url = reverse_lazy("users:register")


class CatalogDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:index")
    login_url = reverse_lazy("users:register")
