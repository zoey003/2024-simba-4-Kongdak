from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Profile , Tag
from django.db.models import Count
from django.http import JsonResponse

def firstpage(request):
    return render(request, 'main/firstpage.html')

def signup_done(request):
    return render(request,'main/signup_done.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return JsonResponse({'success': True}, status=200)
        else:
            return JsonResponse({'success': False, 'error': 'Invalid username or password.'}, status=400)
    return render(request, 'main/firstpage.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            username = request.POST['username']
            password = request.POST['password']
            nickname = request.POST['nickname']
            studentID = request.POST['studentID']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')

            else:
                user = User.objects.create_user(username=username, password=password)
                Profile.objects.create(user=user, nickname=nickname, studentID=studentID)
                messages.success(request, 'Account created successfully.')

                return redirect('signup_done')
    return render(request, 'main/signup.html')


@login_required
def mainpage(request):
    if not request.user.is_authenticated:
        return redirect('firstpage')
    
    # 현재 로그인된 사용자의 프로필 정보 가져오기
    user_profile = get_object_or_404(Profile, user=request.user)

    # 모든 작성자와 그들의 게시물 수를 가져오기
    top_authors = Post.objects.values('author__username')\
        .annotate(post_count=Count('author'))\
        .order_by('-post_count')[:3]

    # 현재 사용자가 작성한 게시물 수
    user_post_count = Post.objects.filter(author=request.user).count()

    # 현재 사용자가 북마크한 게시물 가져오기
    bookmarked_posts = Post.objects.filter(bookmark=request.user)

    context = {
        'user': request.user,
        'user_profile': user_profile,
        'top_authors': top_authors,  # 상위 3명의 작성자와 그들의 게시물 수
        'user_post_count': user_post_count,  # 현재 사용자가 작성한 게시물 수
        'bookmarked_posts': bookmarked_posts,  # 현재 사용자가 북마크한 게시물
    }
    
    return render(request, 'main/mainpage.html', context)

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
    # 현재 로그인된 사용자가 작성한 해당 카테고리와 서브카테고리의 게시물 필터링
    posts = Post.objects.filter(author=request.user, category=category, subcategory=subcategory)
    
    # 해당 카테고리와 서브카테고리에서 상위 3명의 작성자와 그들의 게시물 수를 가져오기
    top_authors = Post.objects.filter(category=category, subcategory=subcategory)\
        .values('author__username')\
        .annotate(post_count=Count('author'))\
        .order_by('-post_count')[:3] # 3위까지 인덱스 늘려주면 됨

    # 모든 작성자와 그들의 게시물 수를 가져오기
    authors_with_post_counts = Post.objects.filter(category=category, subcategory=subcategory)\
        .values('author__username')\
        .annotate(post_count=Count('author'))\
        .order_by('-post_count')

    # 현재 사용자의 해당 카테고리와 서브카테고리에서의 게시물 수
    user_post_count = posts.count()

    context = {
        'category': category,  # 카테고리 이름
        'subcategory': subcategory,  # 서브카테고리 이름
        'posts': posts,  # 현재 로그인된 사용자가 작성한 게시물
        'top_authors': top_authors,  # 상위 3명의 작성자와 그들의 게시물 수
        'authors_with_post_counts': authors_with_post_counts,  # 모든 작성자와 그들의 게시물 수
        'user_post_count': user_post_count,  # 현재 사용자의 게시물 수
    }
    
    # 템플릿을 렌더링하고 컨텍스트 데이터를 전달
    return render(request, 'main/categorypage.html', context)


@login_required #데코레이터: 로그인된 상태에서만 함수 호출, 로그인 되지 않은 경우 로그인 페이지로 리다이렉트
def post_detail(request, category, subcategory, post_id):
    post = get_object_or_404(Post, id=post_id, category=category, subcategory=subcategory)
    return render(request, 'main/post_detail.html', {'post': post})

@login_required
def create_post(request, category, subcategory):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        tags_str = request.POST.get('tags', '')

        if not title or not content:
            messages.error(request, 'Title and content are required.')
        else:
            post = Post.objects.create(
                title=title,
                content=content,
                author=request.user,
                category=category,
                subcategory=subcategory
            )

            # 태그 처리
            if tags_str:
                tags_list = [tag.strip() for tag in tags_str.split('#') if tag.strip()]
                for tag_name in tags_list:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)

            return redirect('categorypage', category=category, subcategory=subcategory)

    return render(request, 'main/create_post.html', {'category': category, 'subcategory': subcategory})

@login_required
def edit_post(request, category, subcategory, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('post_detail', category=category, subcategory=subcategory, post_id=post_id)
    
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        tags_str = request.POST.get('tags', '')

        if not title or not content:
            messages.error(request, 'Title and content are required.')
        else:
            post.title = title
            post.content = content
            post.save()

            # 태그 처리
            post.tags.clear()  # 기존 태그 제거
            if tags_str:
                tags_list = [tag.strip() for tag in tags_str.split('#') if tag.strip()]
                for tag_name in tags_list:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)

            return redirect('post_detail', category=category, subcategory=subcategory, post_id=post.id)
    
    return render(request, 'main/edit_post.html', {'post': post, 'category': category, 'subcategory': subcategory})

@login_required
def delete_post(request, category, subcategory, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author:
        post.delete()
    
    # 쿼리 매개변수에서 next URL을 가져옵니다.
    next_url = request.GET.get('next')
    
    # next URL이 유효하면 해당 URL로 리디렉션, 그렇지 않으면 기본 카테고리 페이지로 리디렉션
    if next_url:
        return redirect(next_url)
    else:
        return redirect('categorypage', category=category, subcategory=subcategory)

@login_required
def post_detail(request, category, subcategory, post_id):
    post = get_object_or_404(Post, id=post_id, category=category, subcategory=subcategory)
    return render(request, 'main/post_detail.html', {'post': post, 'next': request.GET.get('next')})
@login_required
def all_posts(request):
    posts = Post.objects.all()

    bookmarked_posts = request.user.bookmark.all()

    for post in posts:
        post.is_bookmarked = post in bookmarked_posts

    return render(request, 'main/all_posts.html', {'posts': posts})
    

@login_required
def bookmark(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.bookmark.all():
        post.bookmark.remove(request.user)

    else:
        post.bookmark.add(request.user)

    return redirect('all_posts')

@login_required
def search_by_tag(request):
    query = request.GET.get('q', '')
    if query:
        tags = [tag.strip() for tag in query.split('#') if tag.strip()]
        posts = Post.objects.filter(tags__name__in=tags).distinct()
    else:
        posts = Post.objects.none()

    context = {
        'query': query,
        'posts': posts,
    }
    return render(request, 'main/search.html', context)

def check_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)