from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mainpage')
        else:
            messages.error(request, '아이디 혹은 비밀번호가 일치하지 않습니다')
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('main:firstpage')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, '이미 존재하는 ID입니다')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, '계정이 생성되었습니다')
            return redirect('login')
    return render(request, 'accouts/signup.html')
