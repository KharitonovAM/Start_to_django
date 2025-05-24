from django.urls import path
from .views import BlogListView

from .views import *
urlpatterns = [path("blog/", BlogListView.as_view(), name="blog_list"),

               ]