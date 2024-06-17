from django.shortcuts import render, get_object_or_404
from .models import Category, Post


# Create your views here.
def mainpage(request):
    return render(request, 'main/mainpage.html')

def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'category_posts.html', {'category': category, 'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'main/post_detail.html', {'post': post})