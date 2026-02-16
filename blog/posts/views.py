from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Post

# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request,'posts/home.html',{'posts':posts})

def detail(request,id):
    post_data=get_object_or_404(Post,id=id)
    return render(request,'posts/detail.html',{'post':post_data})


