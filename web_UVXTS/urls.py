from django.urls import path
from . import views
from .views import video
from blog import views as blog_views
from tattoo_gallery import views as gallery_views


urlpatterns = [

     path('', views.index, name="index"),
     path('about.html', video, name="about"),

     path('blog.html', blog_views.all_blogs, name="blog"),
     path('blogsingle.html', views.blogsingle, name="blogsingle"),

     path('home.html', views.home, name="home"),
     path('contact.html', views.contact, name="contact"),

     path('gallery.html', gallery_views.gallery, name="gallery"),
     #   path('gallery.html', views.gallery, name="gallery"),
     path('index.html', views.index, name="index"),

     # path('about.html', views.about, name="about"),
     # path('', views.my_form, name='my_form')
     # path('gallery_sketches.html', video),
]