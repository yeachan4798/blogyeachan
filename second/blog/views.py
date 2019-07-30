from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
# Create your views here.

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_data = timezone.datetime.now()
    blog.save()
    return redirect('http://127.0.0.1:8000/'+str(blog.id))

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})
# Create your views here.

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'new.html')

def portfolio(request):
    return render(request, 'portfolio.html')