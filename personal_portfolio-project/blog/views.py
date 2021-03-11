from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    # To show all the blogs
    #blogs = Blog.objects.all()

    # To have how many blogs was written
    blog_count = Blog.objects.count

    # To show the latest 5 ones
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs, 'blog_count':blog_count})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
