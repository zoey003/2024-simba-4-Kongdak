from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Profile , Tag
from django.db.models import Count
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime, timedelta
from .utils import get_weather
from django.utils import timezone
from django.template.loader import render_to_string
from django.utils.timezone import now
from django.http import HttpResponse





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

    ''' 
    # 상위 3명
    top_authors = Post.objects.values('author__username')\
        .annotate(post_count=Count('author'))\
        .order_by('-post_count')[:3]
    '''

    # 현재 사용자가 작성한 게시물 수
    user_post_count = Post.objects.filter(author=request.user).count()

    # 가입일로부터 경과한 일수 계산
    days_since_joined = (datetime.now().date() - request.user.date_joined.date()).days

    # 주간 랭킹 계산
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())  # 이번 주 월요일
    end_of_week = start_of_week + timedelta(days=6)  # 이번 주 일요일
    weekly_top_authors = Post.objects.filter(created_at__date__gte=start_of_week, created_at__date__lte=end_of_week)\
        .values('author__username')\
        .annotate(post_count=Count('author'))\
        .order_by('-post_count')[:3]

    # 날씨 정보 가져오기
    weather_main = get_weather()
    #좋아요 
    bookmarked_posts = request.user.bookmark.all()

    context = {
        'user': request.user,
        'user_profile': user_profile,
        'user_post_count': user_post_count,  # 현재 사용자가 작성한 게시물 수
        'days_since_joined': days_since_joined,  # 가입일로부터 경과한 일수
        'weekly_top_authors': weekly_top_authors,  # 주간 랭킹 상위 3명
        'weather_main': weather_main,  # 날씨 정보
        'bookmarked_posts': bookmarked_posts  # 북마크한 게시물
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

@login_required
def create_post(request, category, subcategory):
    weather_main = get_weather()

    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        tags_str = request.POST.get('tags', '')

        if not title or not content:
            messages.error(request, 'Title and content are required.')
        else:
            # Post 객체 생성 및 저장
            post = Post.objects.create(
                title=title,
                content=content,
                author=request.user,
                category=category,
                subcategory=subcategory,
                weather=weather_main
            )

            # 태그 처리
            if tags_str:
                tags_str = tags_str.replace(' ', '')  # 중간에 있는 모든 공백 제거
                tags_list = [tag.strip() for tag in tags_str.split('#') if tag.strip()]
                for tag_name in tags_list:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)

            return redirect('categorypage', category=category, subcategory=subcategory)

    return render(request, 'main/create_post.html', {
        'category': category,
        'subcategory': subcategory,
        'weather_main': weather_main,
    })


@login_required
def edit_post(request, category, subcategory, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('post_detail', category=category, subcategory=subcategory, post_id=post_id)

    weather_main = get_weather()

    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        tags_str = request.POST.get('tags', '')

        if not title or not content:
            messages.error(request, 'Title and content are required.')
        else:
            # 글 수정 및 날씨 업데이트
            post.title = title
            post.content = content
            post.weather = weather_main
            post.save()

            # 태그 처리
            post.tags.clear()  # 기존 태그 제거
            if tags_str:
                tags_str = tags_str.replace(' ', '')
                tags_list = [tag.strip() for tag in tags_str.split('#') if tag.strip()]
                for tag_name in tags_list:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)

            return redirect('post_detail', category=category, subcategory=subcategory, post_id=post.id)

    return render(request, 'main/edit_post.html', {
        'post': post,
        'category': category,
        'subcategory': subcategory,
        'weather_main': weather_main,
        'tags': ' '.join(f'#{tag.name}' for tag in post.tags.all())
    })


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
    start_year_selected = int(request.GET.get('start_year', 2024))
    end_year_selected = int(request.GET.get('end_year', 2024))
    start_month_selected = int(request.GET.get('start_month', 1))
    end_month_selected = int(request.GET.get('end_month', 12))

    if request.method == 'GET' and (start_year_selected and end_year_selected and start_month_selected and end_month_selected):
        posts = Post.objects.filter(
            author=request.user,
            created_at__year__gte=start_year_selected,
            created_at__year__lte=end_year_selected,
            created_at__month__gte=start_month_selected,
            created_at__month__lte=end_month_selected
        ).order_by('-created_at')
    else:
        posts = Post.objects.filter(author=request.user).order_by('-created_at') 

    bookmarked_posts = request.user.bookmark.all()
    
    for post in posts:
        post.is_bookmarked = post in bookmarked_posts

    return render(request, 'main/all_posts.html', {
        'posts': posts,
        'bookmarked_posts': bookmarked_posts,
        'year_range': range(2024, now().year + 1),
        'months': range(1, 13),
        'start_year_selected': start_year_selected,
        'end_year_selected': end_year_selected,
        'start_month_selected': start_month_selected,
        'end_month_selected': end_month_selected
    })



@login_required
def bookmark(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user in post.bookmark.all():
            post.bookmark.remove(request.user)
            is_bookmarked = False
        else:
            post.bookmark.add(request.user)
            is_bookmarked = True

        data = {'success': True, 'is_bookmarked': is_bookmarked}
        return JsonResponse(data)

    return JsonResponse({'success': False, 'error': 'Invalid request'})


@login_required
def search_by_tag(request):
    query = request.GET.get('q', '')
    if query:
        # 태그에서 띄어쓰기 제거
        query = query.replace(' ', '')
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
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        username = data.get('username', None)
        is_taken = User.objects.filter(username=username).exists()
        response = {
            'is_taken': is_taken
        }
        return JsonResponse(response)
    return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)


# def filter_by_date(request):
#     if request.method == 'GET':
#         start_year_selected = int(request.GET.get('start_year', 2024))
#         end_year_selected = int(request.GET.get('end_year', 2024))
#         start_month_selected = int(request.GET.get('start_month', 1))
#         end_month_selected = int(request.GET.get('end_month', 12))

#         posts = Post.objects.filter(
#             author=request.user,
#             created_at__year__gte=start_year_selected,
#             created_at__year__lte=end_year_selected,
#             created_at__month__gte=start_month_selected,
#             created_at__month__lte=end_month_selected
#         ).order_by('-created_at') 
#         bookmarked_posts = request.user.bookmark.all()
        
#         for post in posts:
#             post.is_bookmarked = post in bookmarked_posts

        

#         html_content = render_to_string('main/all_posts.html', {
#             'posts': posts,
#             'start_year_selected': start_year_selected,
#             'end_year_selected': end_year_selected,
#             'start_month_selected': start_month_selected,
#             'end_month_selected': end_month_selected
#         })
        
#         return HttpResponse(html_content)
#     else:
#         return redirect('all_posts')
    

 