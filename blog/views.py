from django.shortcuts import redirect, render
from .models import *
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import PostForms

# Create your views here.

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now())
    return render(request,'blog/post_list.html',{'posts':posts})


def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request,'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
    else:
        form = PostForms()
    
    return render(request,'blog/post_edit.html',{'form':form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForms(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForms(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

