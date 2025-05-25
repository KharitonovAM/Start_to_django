from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publication


class BlogListView(ListView):
    model = Publication

class BlogDetailView(DetailView):
    model = Publication