from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Post
from . forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def index(request):
    post=Post.objects.all()
    return render(request,"index.html",{'post':post})
def post(request,id):
    post=Post.objects.get(id=id)
    return render(request,"post.html",{'post':post})
@login_required
def add(request):
    add=PostForm()
    if request.method =='POST':
        add = PostForm(request.POST, request.FILES)
        if add.is_valid():
            add.save()
            return redirect("add")
    return render(request,"add.html",{'add':add})
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return index(request)  
def edit(request, id):
    post = Post.objects.get(id=id)
    form=PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return index(request) 
    return render(request,"edit.html",{'form':form})
def register(request):
    form=UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request,"register.html",{'form':form})