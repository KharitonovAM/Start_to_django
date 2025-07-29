from django.urls import path

from .apps import BlogConfig
from .views import (BlogCreateView, BlogDeleteView, BlogDetailView,
                    BlogListView, BlogUpdateView)

app_name = BlogConfig.name

urlpatterns = [
    path("blog/", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/create", BlogCreateView.as_view(), name="create_blog"),
    path("blog/<int:pk>/update", BlogUpdateView.as_view(), name="update_blog"),
    path("blog/<int:pk>/delete", BlogDeleteView.as_view(), name="delete_blog"),
]
