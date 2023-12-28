from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path("home", home)
    path("home", home),
    path("your-blogs", showBlogs),
    path("your-blogs/<id>", showOneBlog),
    path("add-blog", addBlog),
    path("edit-blog/<id>", updateBlog),
    path("delete-blog/<id>", deleteBlog),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
