from django.urls import path
from .views import BlogListView, BlogDetailView
from .apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [path("blog/", BlogListView.as_view(), name="blog_list"),
               path("blog/<int:pk>", BlogDetailView.as_view(), name='blog_detail'),
               ]