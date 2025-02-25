from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post, Thread
from .forms import PostForm, LoginForm, ThreadForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = LoginForm()
    return render(request, 'posts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'posts/my_posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    can_edit = request.user == post.author
    can_delete = request.user == post.author or request.user.is_superuser
    return render(request, 'posts/post_detail.html', {
        'post': post, 
        'can_edit': can_edit,
        'can_delete': can_delete
    })

@login_required
def post_create(request):
    # Check if any threads exist, if not, create a default one
    if Thread.objects.count() == 0:
        Thread.objects.create(name="General Discussion")
        
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.user != post.author and not request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to delete this post")
        
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
        
    return render(request, 'posts/post_confirm_delete.html', {'post': post})

@login_required
def thread_list(request):
    threads = Thread.objects.all().order_by('name')
    return render(request, 'posts/thread_list.html', {'threads': threads})

@login_required
def thread_create(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    else:
        form = ThreadForm()
    return render(request, 'posts/thread_form.html', {'form': form})