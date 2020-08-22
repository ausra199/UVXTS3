
from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path ('', views.all_blogs, name="blog.html"),
    path ('<int:blog_id>', views.blog_detail, name="blog_detail"),
    path('incl_blogsingle_all_img.html', views.incl_blogsingle_all_img, name="incl_blogsingle_all_img")
]

