from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


def contact(request):
    return render(request, "contacts.html")


def products(request, pk):
    product = Product.objects.get(pk=pk)
    contex = {"product": product}
    return render(request, "products.html", context=contex)


class CatalogListView(ListView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class CatalogDetailView(DetailView):
    model = Product

