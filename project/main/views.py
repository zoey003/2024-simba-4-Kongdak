from django.shortcuts import render, get_object_or_404
from .models import Category, Post

from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Post
# Create your views here.
def mainpage(request): #메인페이지 랜더링
    return render(request, 'main/mainpage.html')

def category_posts(request, category_id): # 카테고리 글 목록 함수
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'category_posts.html', {'category': category, 'posts': posts})

def post_detail(request, post_id): # 글 본문 함수
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'main/post_detail.html', {'post': post})

def create(request): # 글 create
    new_post = Post()

    new_post.title = request.POST['title']
    new_post.body=request.POST['body']
    new_post.pub_date=timezone.now()

    new_post.save()

    return redirect('main:post_detail',new_post.id) ## 게시글 작성 끝나면 연결할 페이지

def new_post(request): # 글 create 페이지 함수
    return render(request,'main/new-post.html')

def edit(request, id): # 글 수정 페이지 랜더링 함수
    edit_post = Post.objects.get(pk=id)
    return render(request,'main/edit.html',{'post':edit_post})

def update(request, id): #글 update 함수 
    update_post=Post.objects.get(pk=id)

    update_post.title = request.POST['title']
    update_post.body = request.POST['body']
    update_post.pub_date=timezone.now()

    update_post.save()

    return redirect('main:post_detail',update_post.id) ## 게시글 작성 끝나면 연결할 페이지 

def delete(request, id):
    delete_post = Post.objects.get(pk=id)
    delete_post.delete()
    return redirect('main:category_posts') # 삭제후 이동할 페이지

