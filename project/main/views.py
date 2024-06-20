from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def firstpage(request):
    return render(request, 'main/firstpage.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('mainpage')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'main/firstpage.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            username = request.POST['username']
            password = request.POST['password']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Account created successfully.')
                return redirect('firstpage')
    return render(request, 'main/signup.html')

def mainpage(request):
    if not request.user.is_authenticated:
        return redirect('firstpage')
    return render(request, 'main/mainpage.html', {'user': request.user})

def secondpage_a(request):
    if not request.user.is_authenticated:
        return redirect('firstpage')
    return render(request, 'main/secondpage_a.html')

def secondpage_b(request):
    if not request.user.is_authenticated:
        return redirect('firstpage')
    return render(request, 'main/secondpage_b.html')

def secondpage_c(request):
    if not request.user.is_authenticated:
        return redirect('firstpage')
    return render(request, 'main/secondpage_c.html')

def categorypage(request, category, subcategory):
    posts = Post.objects.filter(author = request.user,category=category, subcategory=subcategory)
    context ={
        'category': category,
        'subcategory': subcategory,
        'posts': posts,
    }
    return render(request, 'main/categorypage.html',context)

@login_required #데코레이터: 로그인된 상태에서만 함수 호출, 로그인 되지 않은 경우 로그인 페이지로 리다이렉트
def post_detail(request, category, subcategory, post_id):
    post = get_object_or_404(Post, id=post_id, category=category, subcategory=subcategory)
    return render(request, 'main/post_detail.html', {'post': post})

@login_required
def create_post(request, category, subcategory):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category = category
            post.subcategory = subcategory
            post.save()
            # 작성한 글이 속한 카테고리 페이지로 리다이렉션
            return redirect('categorypage', category=category, subcategory=subcategory)
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form, 'category': category, 'subcategory': subcategory})