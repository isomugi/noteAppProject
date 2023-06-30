from django.shortcuts import render, redirect

# Create your views here.
#urls.py で紐づけられた関数が呼び出された時の挙動を決定する
#基本的にはhtmlを返す return render(request, 'ファイルの場所', context)
from django.http import HttpResponse
from .models import Post, PostModel
from .forms import PostForm, LoginForm, RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')
    
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('note_app:index')
    else:
        form = PostForm()
    
    context = {
        'latest_post_list': latest_post_list,
        'form': form,
    }
    
    return render(request, 'note_app/index.html', context)

def create(request):
    if not request.user.is_authenticated:
        return redirect('note_app:login')
    return render(request, 'note_app/create.html')

def delete(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    if not request.user.is_authenticated:
        return redirect('note_app:login')
    elif request.method == 'POST':
        post.delete()
        return redirect('note_app:index')
    return render(request, 'note_app/delete.html', {'post': post})
    
    
def post(request):
    if not request.user.is_authenticated:
        return redirect('note_app:login')
    elif request.method == 'POST':
        form = PostModel(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            """ title = request.POST['title']
            content = request.POST['content']
            post = Post.objects.create(title = title, content = content) """
            return redirect('note_app:detail', post_id = post.id)
    else:
        form = PostModel()
    #posts = Post.objects.all().order_by('-created_at')
    return render(request, 'note_app/post.html', {'form': form})#, 'posts': posts

def detail(request, post_id):
    
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'note_app/detail.html', {'post': post})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('note_app:index')
    elif request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('note_app:index')
    else:
        form = LoginForm()
    return render(request, 'note_app/login.html', {'form': form})

def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('note_app:login')
    elif request.method == 'POST':
        logout(request)
    return redirect('note_app:index')

def register(request):
    if request.user.is_authenticated:
        return redirect('note_app:index')
    elif request.method == 'POST':
        form = RegisterForm(data = request.POST)
        if form.is_valid():
            form.save()
            """ username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            login(request, user) """
            return redirect('note_app:index')
    else:
        form = RegisterForm()
    return render(request, 'note_app/register.html', {'form': form})
