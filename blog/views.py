from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')

    context = {
        'blogs':blogs
    }
    return render(request, 'blog.html', context)

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog':blog
    }
    return render(request, 'blogsingle.html', context)

def incl_blogsingle_all_img(request):
    blogs = Blog.objects.order_by('-date')

    context = {
        'blogs':blogs
    }
    return render(request, 'incl_blogsingle_all_img.html', context)
