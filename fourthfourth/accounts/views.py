from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')

def home(request):
      blogs=Blog.objects
      # 블로그 모든 글들을 대상으로
      blog_list = Blog.objects.all()
      # 블로그 객체 세 개를 한 페이지로 자르기
      paginator = Paginator(blog_list, 3)
      # request된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
      page = request.GET.get('page')
      # request된 페이지를 얻어낸 뒤 return 해준다
      posts = paginator.get_page(page)
      return render(request, 'home.html', {'blogs':blogs, 'posts':posts})
