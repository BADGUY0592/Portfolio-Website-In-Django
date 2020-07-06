from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_home(request):
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/bloghome.html',{'blogs':blogs})

def blog_page(request,blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})
