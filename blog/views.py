from django.shortcuts import render
from .models import Blog

def blog_home(request):
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/bloghome.html',{'blogs':blogs})
