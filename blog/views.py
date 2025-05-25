from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Publication


class BlogListView(ListView):
    model = Publication

class BlogDetailView(DetailView):
    model = Publication


class BlogCreateView(CreateView):
    model = Publication
    fields = ('title', 'content', 'preview', 'create_data', 'is_publicated', 'number_shows')
    success_url = reverse_lazy('blog:blog_list')