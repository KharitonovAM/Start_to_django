from django.shortcuts import render
from django.views.generic import ListView

from .models import Product

# Create your views here.


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contacts.html")


def base_page(reguest):
    return render(reguest, "base.html")


def products(request, pk):
    product = Product.objects.get(pk=pk)
    contex = {"product": product}
    return render(request, "products.html", context=contex)


# def list_products(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "home.html", context=context)

class CatalogListView(ListView):
    model = Product
