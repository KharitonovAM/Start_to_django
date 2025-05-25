from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Publication


class BlogListView(ListView):
    model = Publication

    def get_queryset(self):
        return Publication.objects.filter(is_publicated=True)


class BlogDetailView(DetailView):
    model = Publication
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_shows += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Publication
    fields = ("title", "content", "preview", "create_data", 'is_publicated', 'number_shows')
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = Publication
    fields = ('title', 'content', 'preview', 'create_data', 'is_publicated', 'number_shows')
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

