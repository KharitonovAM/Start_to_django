from django.shortcuts import render
from django.views.generic import ListView
from .models import Publication


class BlogListView(ListView):
    model = Publication

