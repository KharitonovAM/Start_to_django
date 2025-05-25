from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView
from .apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [path("blog/", BlogListView.as_view(), name="blog_list"),
               path("blog/<int:pk>", BlogDetailView.as_view(), name='blog_detail'),
               path("blog/create", BlogCreateView.as_view(), name='create_blog'),
               path('blog/<int:pk>/update', BlogUpdateView.as_view(), name='update_blog'),
               ]